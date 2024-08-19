// the search button toggle from x to the search bar itself
let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');
// the bar menu on small screens
let menu = document.querySelector('#menu-bar');
let navbar = document.querySelector('.navbar');

window.onscroll = () => {
    searchBtn.classList.remove('bx-x');
    searchBar.classList.remove('active');
}
// the search button toggle from x to the search bar itself
searchBtn.addEventListener('click', () => {
    searchBtn.classList.toggle('bx-x');
    searchBar.classList.toggle('active');
});

// the bar menu on small screens
menu.addEventListener('click', () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
});
