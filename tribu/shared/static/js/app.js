const profileBtn = document.querySelector(".user-box");
const menu = document.querySelector(".user-nav");

profileBtn.addEventListener("click", (e) => {
  e.stopPropagation();
  menu.style.display = "block";
});

document.addEventListener("click", () => {
  menu.style.display = "none";
});
