"use-strict";
console.log("this is connected");
// select elements
const toggleBtn = document.querySelector(".nav__toggle-btn");
const menuList = document.querySelector(".nav__items");

// toggle navbar
toggleBtn.addEventListener("click", () => {
  menuList.classList.toggle("active");
});
