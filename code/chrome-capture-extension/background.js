// Nexus Capture - background service worker
//
// Waits for "CAPTURE" messages from content.js, and uploads them to the
// self-hosted Nexus server, using whatever token the user has saved on
// the options page.

const CAPTURE_ENDPOINT = "https://nexus.needpedia.org/capture";
const TOKEN_STORAGE_KEY = "captureToken";

chrome.runtime.onMessage.addListener((message) => {
  if (!message || message.type !== "CAPTURE") {
    return;
  }

  chrome.storage.local.get(TOKEN_STORAGE_KEY, (result) => {
    const token = result[TOKEN_STORAGE_KEY];

    // No token configured yet: stay quiet. No error, no notification.
    if (!token) {
      return;
    }

    fetch(CAPTURE_ENDPOINT, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-Capture-Token": token,
      },
      body: JSON.stringify({
        claude_id: message.claude_id,
        title: message.title,
        messages: message.messages,
      }),
    }).catch(() => {
      // Ignore failures - no retry logic needed. The next mutation
      // cycle on the page will naturally trigger another capture
      // attempt and resend.
    });
  });
});
