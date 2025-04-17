// Scroll to Top Function code

function scrollToTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
}

// Dark mode code
window.onload = function () {
    const btnIcon = document.querySelector("#darkModeBtn i");
    const isDark = localStorage.getItem("dark-mode") === "enabled";

    if (isDark) {
      document.body.classList.add("dark-mode");
      btnIcon.classList.remove("fa-moon");
      btnIcon.classList.add("fa-sun");
    } else {
      btnIcon.classList.remove("fa-sun");
      btnIcon.classList.add("fa-moon");
    }
  };

  function toggleDarkMode() {
    const btnIcon = document.querySelector("#darkModeBtn i");
    const isNowDark = document.body.classList.toggle("dark-mode");

    if (isNowDark) {
      btnIcon.classList.remove("fa-moon");
      btnIcon.classList.add("fa-sun");
      localStorage.setItem("dark-mode", "enabled");
    } else {
      btnIcon.classList.remove("fa-sun");
      btnIcon.classList.add("fa-moon");
      localStorage.setItem("dark-mode", "disabled");
    }
  }