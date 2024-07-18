var toggleButton = document.querySelector("#toggle-dark-mode-button");

function toggleDarkMode() {
    document.body.classList.toggle("dark-mode");
    document.querySelector("header").classList.toggle("dark-mode");
    document.querySelector("footer").classList.toggle("dark-mode");
    document.querySelectorAll("section").forEach((section) => section.classList.toggle("dark-mode"));
    document.querySelectorAll("button").forEach((btn) => btn.classList.toggle("dark-mode"));
    document.querySelectorAll("a").forEach((link) => link.classList.toggle("dark-mode"));
}

if (body.classList.contains("dark-mode")) {
    toggleButton.textContent = "Mudar para o modo claro";
} else {
    toggleButton.textContent = "Mudar para o modo escuro";
}
