// Scroll to Top Function code

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Dark mode code
window.onload = function () {
    const isDark = localStorage.getItem("dark-mode") === "enabled";
    if (isDark) {
        document.body.classList.add("dark-mode");
        document.getElementById("darkModeBtn").textContent = "🌞";
    }
};

function toggleDarkMode() {
    const btn = document.getElementById("darkModeBtn");
    const isDark = document.body.classList.toggle("dark-mode");

    // Change icon
    btn.textContent = isDark ? "🌞" : "🌙";

    // Save preference
    localStorage.setItem("dark-mode", isDark ? "enabled" : "disabled");
}