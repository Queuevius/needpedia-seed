// Nexus Capture - options page script
//
// Saves the capture token to chrome.storage.local, and shows a masked
// preview of it if one is already saved (so Tony can tell it's set
// without the full token being visible on screen).

const TOKEN_STORAGE_KEY = "captureToken";

const tokenInput = document.getElementById("token");
const saveButton = document.getElementById("save");
const statusEl = document.getElementById("status");

// Holds the real, unmasked token once loaded from storage.
let storedToken = null;

// True once the user actually types in the field, so we know the
// input no longer just holds our masked display value.
let userEdited = false;

function maskToken(token) {
  if (token.length <= 8) {
    return "•".repeat(token.length);
  }
  return token.slice(0, 4) + "•".repeat(token.length - 8) + token.slice(-4);
}

// Pre-fill the input (masked) if a token is already stored.
chrome.storage.local.get(TOKEN_STORAGE_KEY, (result) => {
  const existing = result[TOKEN_STORAGE_KEY];
  if (existing) {
    storedToken = existing;
    tokenInput.value = maskToken(existing);
  }
});

tokenInput.addEventListener("input", () => {
  userEdited = true;
});

saveButton.addEventListener("click", () => {
  // If the user never touched the field, keep the existing token
  // instead of saving the masked placeholder text over it.
  const tokenToSave = userEdited ? tokenInput.value.trim() : storedToken;

  if (!tokenToSave) {
    return;
  }

  chrome.storage.local.set({ [TOKEN_STORAGE_KEY]: tokenToSave }, () => {
    storedToken = tokenToSave;
    userEdited = false;
    tokenInput.value = maskToken(tokenToSave);

    statusEl.style.visibility = "visible";
    setTimeout(() => {
      statusEl.style.visibility = "hidden";
    }, 2000);
  });
});
