// Nexus Capture - content script
// Runs only on https://claude.ai/* (see manifest.json content_scripts).
//
// S28: captures via claude.ai's own data endpoint instead of scraping
// the rendered page. DOM scraping could never see code boxes rendered
// as MCP-widget iframes (different origin). This fetches the whole
// conversation as structured JSON using the login session already in
// the browser - code arrives already fenced as text.

// How long the page must be quiet before we capture.
const IDLE_MS = 4000;

// Remembers the last fingerprint sent per conversation, so we don't
// re-send an unchanged conversation every time the page twitches.
const lastSentFingerprint = {};

let idleTimer = null;

function scheduleCapture() {
  if (idleTimer) {
    clearTimeout(idleTimer);
  }
  idleTimer = setTimeout(runCapture, IDLE_MS);
}

// Pulls the conversation ID out of a URL like
// https://claude.ai/chat/abc-123-def
function getConversationIdFromUrl() {
  const match = window.location.pathname.match(/\/chat\/([^/?#]+)/);
  return match ? match[1] : null;
}

// Fetches the org UUID for the logged-in account. The user's session
// cookies ride along automatically (same-origin request).
async function fetchOrgId() {
  const res = await fetch("https://claude.ai/api/organizations");
  if (!res.ok) {
    return null;
  }
  const orgs = await res.json();
  return orgs && orgs[0] ? orgs[0].uuid : null;
}

// Fetches ONE full conversation. rendering_mode=messages is what makes
// replies come back complete (with code fenced) rather than flattened.
async function fetchConversation(orgId, claudeId) {
  const url =
    "https://claude.ai/api/organizations/" +
    orgId +
    "/chat_conversations/" +
    claudeId +
    "?tree=True&rendering_mode=messages&render_all_tools=true";
  const res = await fetch(url);
  if (!res.ok) {
    return null;
  }
  return res.json();
}

// Turns one API message object into { role, content }.
//
// Each message has a `content` array of typed blocks. We keep only
// `type === "text"` blocks (prose + already-fenced code) and join them
// in order. tool_use / tool_result blocks (web-search activity,
// visualize widgets, etc.) are skipped as noise.
function extractMessage(msg) {
  const role = msg.sender === "human" ? "user" : "assistant";

  const blocks = Array.isArray(msg.content) ? msg.content : [];
  let content = blocks
    .filter((b) => b && b.type === "text" && typeof b.text === "string")
    .map((b) => b.text)
    .join("\n\n")
    .trim();

  // Fallback: if no text blocks (unusual layout), use the message's
  // top-level text field if present.
  if (!content && typeof msg.text === "string") {
    content = msg.text.trim();
  }

  // Represent any attached files as a literal placeholder string, e.g.
  // "[file uploaded: report.pdf]". Real contents are a later milestone.
  const files = Array.isArray(msg.files) ? msg.files : [];
  files.forEach((f) => {
    const name = f && (f.file_name || f.name);
    if (name) {
      content += `\n[file uploaded: ${name}]`;
    }
  });
  const attachments = Array.isArray(msg.attachments) ? msg.attachments : [];
  attachments.forEach((a) => {
    const name = a && (a.file_name || a.name);
    if (name) {
      content += `\n[file uploaded: ${name}]`;
    }
  });

  return { role, content: content.trim() };
}

// Fetches and shapes the current conversation into
// { claudeId, title, messages }, or null if not on a conversation page
// / the fetch failed.
async function extractConversation() {
  const claudeId = getConversationIdFromUrl();
  if (!claudeId) {
    return null; // Not on a conversation page (e.g. the new-chat screen).
  }

  const orgId = await fetchOrgId();
  if (!orgId) {
    return null;
  }

  const convo = await fetchConversation(orgId, claudeId);
  if (!convo) {
    return null;
  }

  const rawMessages = Array.isArray(convo.chat_messages)
    ? convo.chat_messages
    : [];
  const messages = rawMessages
    .map(extractMessage)
    .filter((m) => m.content.length > 0);

  if (messages.length === 0) {
    return null;
  }

  const firstUserMessage = messages.find((m) => m.role === "user");
  const fallbackTitle = firstUserMessage
    ? firstUserMessage.content.slice(0, 60)
    : "Untitled conversation";
  const title = convo.name && convo.name.trim() ? convo.name.trim() : fallbackTitle;

  return { claudeId, title, messages };
}

// Small, fast, non-cryptographic string hash (djb2), for change
// detection only.
function hashString(str) {
  let hash = 5381;
  for (let i = 0; i < str.length; i++) {
    hash = (hash * 33) ^ str.charCodeAt(i);
  }
  return (hash >>> 0).toString(16);
}

function computeFingerprint(conversation) {
  const lastMessage = conversation.messages[conversation.messages.length - 1];
  return `${conversation.messages.length}:${hashString(lastMessage.content)}`;
}

async function runCapture() {
  let conversation;
  try {
    conversation = await extractConversation();
  } catch (e) {
    return; // Network hiccup or unexpected shape: next mutation retries.
  }
  if (!conversation) {
    return;
  }

  const fingerprint = computeFingerprint(conversation);
  if (lastSentFingerprint[conversation.claudeId] === fingerprint) {
    return; // Nothing new since the last time we sent this conversation.
  }

  chrome.runtime.sendMessage({
    type: "CAPTURE",
    claude_id: conversation.claudeId,
    title: conversation.title,
    messages: conversation.messages,
  });

  lastSentFingerprint[conversation.claudeId] = fingerprint;
}

const observer = new MutationObserver(() => {
  scheduleCapture();
});

observer.observe(document.body, {
  childList: true,
  subtree: true,
  characterData: true,
});

// Also try once shortly after load, in case the page was already still
// (e.g. the extension was just installed/reloaded).
scheduleCapture();
