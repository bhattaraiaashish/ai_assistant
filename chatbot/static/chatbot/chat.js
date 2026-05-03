document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("chat-form");
    const input = document.getElementById("messageInput");
    const sendButton = document.getElementById("sendButton");
    const box = document.getElementById("chat-box");

    if (box) {
        box.scrollTop = box.scrollHeight;
    }

    if (!input) {
        return;
    }

    const resizeInput = function () {
        input.style.height = "auto";
        input.style.height = `${Math.min(input.scrollHeight, 160)}px`;
    };

    input.addEventListener("input", resizeInput);
    resizeInput();

    input.addEventListener("keydown", function (event) {
        if (event.key === "Enter" && !event.shiftKey) {
            event.preventDefault();
            if (form && input.value.trim()) {
                form.requestSubmit();
            }
        }
    });

    if (form && sendButton) {
        form.addEventListener("submit", function () {
            sendButton.textContent = "Sending";
            sendButton.disabled = true;
        });
    }
});
