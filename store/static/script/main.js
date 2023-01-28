let headlis = document.querySelectorAll("header .headLink li");
let menus = document.querySelectorAll("header .menu");

headlis.forEach((li) => {
  li.onclick = () => {
    // get id from clicked li
    let id = li.getAttribute("data-id");
    menus.forEach((menu) => {
      // if menu that her id isn't the clicked and it steel show ,
      //  hide it by adding a hidden class
      if (
        menu.getAttribute("data-id") !== id &&
        !menu.classList.contains("hidden")
      ) {
        menu.classList.add("hidden");
      }

      if (menu.getAttribute("data-id") == id) {
        menu.classList.toggle("hidden");
      }
    });
  };
});

document.addEventListener("click", (e) => {
  console.log(e.target);
  if (!e.target.getAttribute("data-id")) {
    menus.forEach((menu) => {
      menu.classList.add("hidden");
    });
  }
});
