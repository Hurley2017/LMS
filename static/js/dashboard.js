document.addEventListener("DOMContentLoaded", function() {
    const userOptions = document.querySelector(".navbar-user");
    userOptions.addEventListener("click", function() {
      this.classList.toggle("active");
    });
  });
  