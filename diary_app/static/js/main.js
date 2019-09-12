function toggleBurger() {
    var burger = $('.burger');
    var menu = $('.navbar-menu');
    burger.toggleClass('is-active');
    menu.toggleClass('is-active');
}

function goback() {
    history.back();
}

window.onload = () => {
    document.querySelector(".hero").classList.add("header-image");
};