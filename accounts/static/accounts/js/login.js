document.addEventListener("DOMContentLoaded", function () {
    document.addEventListener("keydown", function (e) {
        if (e.key === "Enter") {
            const form = document.querySelector("form");
            if (form) form.requestSubmit();
        }
    });

    const messages = document.querySelectorAll(".alert");

    if (messages.length > 0) {
        setTimeout(() => {
            messages.forEach(msg => {
                msg.style.transition = "0.5s";
                msg.style.opacity = "0";
                msg.style.transform = "translateY(-10px)";

                setTimeout(() => {
                    msg.remove();
                }, 500);
            });
        }, 10000);
    }

    window.togglePassword = function (id) {
        const input = document.getElementById(id);
        if (!input) return;
        input.type = input.type === "password" ? "text" : "password";
    };

    const password = document.getElementById("password");
    const confirmPassword = document.getElementById("confirm_password");
    const bar = document.getElementById("strengthBar");
    const errorText = document.getElementById("errorText");

    function updatePasswordState() {
        if (!password || !bar) return;

        const val = password.value;
        let strength = 0;

        if (val.length > 5) strength += 30;
        if (/[A-Z]/.test(val)) strength += 20;
        if (/[0-9]/.test(val)) strength += 20;
        if (/[@$!%*?&]/.test(val)) strength += 30;

        bar.style.width = strength + "%";

        if (strength < 40) {
            bar.style.background = "red";
        } else if (strength < 70) {
            bar.style.background = "orange";
        } else {
            bar.style.background = "limegreen";
        }

        if (confirmPassword && errorText) {
            errorText.textContent =
                confirmPassword.value && confirmPassword.value !== val
                    ? "Passwords do not match."
                    : "";
        }
    }

    if (password) password.addEventListener("input", updatePasswordState);
    if (confirmPassword) confirmPassword.addEventListener("input", updatePasswordState);

    const registerbtn = document.getElementById("register-btn");

    if (registerbtn) {
        registerbtn.addEventListener("click", function () {
            registerbtn.innerText = "Creating account...";
            registerbtn.style.opacity = "0.7";
        });
    }

    const loginbtn = document.getElementById("login-btn");

    if (loginbtn) {
        loginbtn.addEventListener("click", function () {
            loginbtn.innerText = "Logging in...";
            loginbtn.style.opacity = "0.7";
        });
    }
});
