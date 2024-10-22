// Handling menu bar
const menu = document.querySelector('#menu-bar');
const navbar = document.querySelector('.navbar');
// video display
const videoBtn = document.querySelectorAll('.vid-btn');

// Removing active classes
window.onscroll = () => {
    menu.classList.remove('bx-x');
    navbar.classList.remove('active');
    loginForm.classList.remove('active');
};

// Switch from x to menu bar
menu.addEventListener('click', () => {
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
});

// Rate us form
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

// about us slider
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

const videos = document.querySelectorAll('.video');
let currentVideo = 0;

// Function to play the next video
function playNextVideo() {
    videos[currentVideo].style.display = 'none'; // Hide the current video
    currentVideo = (currentVideo + 1) % videos.length; // Move to the next video
    videos[currentVideo].style.display = 'block'; // Show the next video
    
    // Automatically play the next video after the current one ends
    videos[currentVideo].play();
}

// Initially play the first video
videos[currentVideo].style.display = 'block';
videos[currentVideo].play();

// Set an event listener to play the next video when the current one ends
videos[currentVideo].addEventListener('ended', playNextVideo);
