// Handling menu bar
const menu = document.querySelector('#menu-bar');
const navbar = document.querySelector('.navbar');
// video display
const videoBtn = document.querySelectorAll('.vid-btn');
// login form
const formBtn = document.querySelector('#login-btn');
const loginForm = document.querySelector('.login-form-container');
const formClose= document.querySelector('#form-close');

// Removing active classes
window.onscroll = () => {
    menu.classList.remove('bx-x');
    navbar.classList.remove('active');
    loginForm.classList.remove('active');
};

// switch from x to menu bar
menu.addEventListener('click', () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
});
// closing and opening the login form
formBtn.addEventListener('click', () => {
    loginForm.classList.add('active');
});

formClose.addEventListener('click', () => {
    loginForm.classList.remove('active');
});

// rate us form
document.getElementById('rating-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way
    
    const rating = document.querySelector('input[name="rating"]:checked');
    const ratingMessage = document.getElementById('rating-message');
    
    if (rating) {
        const ratingValue = rating.value;
        ratingMessage.textContent = `Thank you for rating us ${ratingValue} star${ratingValue > 1 ? 's' : ''}!`;
        ratingMessage.style.color = 'green';
    } else {
        ratingMessage.textContent = 'Please select a rating before submitting.';
        ratingMessage.style.color = 'red';
    }
});


    // review slider
    var swiper = new Swiper(".reviews-slider", {
        spaceBetween: 20,
        loop: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: true,
        },
        breakpoints: {
            640: {
                slidesPerView: 1,
            },
            768: {
                slidesPerView: 2,
            },
            1024: {
                slidesPerView: 3,
            },
        },
        
    });


