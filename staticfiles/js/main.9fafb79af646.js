function toggleBurger() {
    var burger = $('.burger');
    var menu = $('.navbar-menu');
    burger.toggleClass('is-active');
    menu.toggleClass('is-active');
}

function delete_No() {
    history.back();
}