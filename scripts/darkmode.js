function toggleDarkMode() {
    const body = document.body;
    const isDark = body.classList.toggle("dark");
    localStorage.setItem("theme", isDark ? "dark" : "light");
    updateToggleIcon(isDark);
    showToast(isDark ? "Dark mode enabled" : "Light mode enabled");
}

function updateToggleIcon(isDark) {
    const toggleBtn = document.querySelector(".toggle");
    toggleBtn.textContent = isDark ? "☀️" : "🌙";
}

function showToast(message) {
    const toast = document.getElementById("toast");
    toast.textContent = message;
    toast.style.display = "block";
    setTimeout(() => {
        toast.style.display = "none";
    }, 2000);
}

window.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme");
    const isDark = savedTheme === "dark";
    if (isDark) document.body.classList.add("dark");
    updateToggleIcon(isDark);

    // Spinner logic for form submission
    const forms = document.querySelectorAll("form");
    forms.forEach(form => {
        form.addEventListener("submit", () => {
            document.getElementById("spinner").style.display = "block";
        });
    });
});
