document.addEventListener("DOMContentLoaded", function () {

    console.log("HoklabariAI UI Loaded 🚀");

    // Example: smooth scroll (optional enhancement)
    let links = document.querySelectorAll("a");

    links.forEach(link => {
        link.addEventListener("click", function () {
            console.log("Navigating to:", link.href);
        });
    });

    let chatBox = document.getElementById("chat-box");

    if (chatBox) {
        chatBox.scrollTop = chatBox.scrollHeight;
    }


});