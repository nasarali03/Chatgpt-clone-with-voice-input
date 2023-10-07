const micButton = document.querySelector("#mic-btn");
const recognition = new webkitSpeechRecognition();
recognition.lang = "en-US";
const activeLanguageElement = document.getElementById("active-language");
micButton.addEventListener("click", () => {
  // const supportedLanguages = ["en-US", "es-ES", "fr-FR", "ur-PK"];

  if (!recognition.continuous) {
    recognition.start();
    micButton.classList.add("listening");
  } else {
    recognition.stop();
    micButton.classList.remove("listening");
  }
});

recognition.onresult = function (event) {
  const speechToText = event.results[0][0].transcript;
  chatInput.value = speechToText;
  // handleOutgoingChat();
};
recognition.onend = function () {
  micButton.classList.remove("listening");
};
micButton.addEventListener("contextmenu", (e) => {
  e.preventDefault();
  toggleRecognitionLanguage();
});

function toggleRecognitionLanguage() {
  // Get the current language code
  const currentLangCode = recognition.lang;

  // Find the next supported language in your list (you can expand the list)
  const supportedLanguages = ["en-US", "ur-PK"];
  const currentLangIndex = supportedLanguages.indexOf(currentLangCode);
  const nextLangIndex = (currentLangIndex + 1) % supportedLanguages.length;
  const nextLangCode = supportedLanguages[nextLangIndex];

  // Update the recognition language
  recognition.lang = nextLangCode;
  activeLanguageElement.textContent = `${getLanguageName(nextLangCode)}`;
  console.log(`Switched to ${nextLangCode} language`);
}
function getLanguageName(langCode) {
  switch (langCode) {
    case "en-US":
      return "en";
    case "ur-PK":
      return "ur";
    default:
      return "Unknown";
  }
}
