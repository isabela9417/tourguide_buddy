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


// videos on auto-play for 5s
    // Array of video sources
    const videoSources = [
        { src: 'videos/457446_South Africa_Africa_1920x1080.mp4', caption: 'Search for your destination, as it awaits you...' },
        { src: 'videos/463049_Elephant_Elephants_1920x1080.mp4', caption: 'Wild life showing the beauty of the wilderness...' },
        { src: 'videos/6013749_Nature_Forest_3840x2160.mp4', caption: 'Enchanting forest landscapes, natural hot-springs' },
        { src: 'videos/1112734_Windy_Roast_3840x2160.mp4', caption: 'Camping sites, where family and friends matters...' },
        { src: 'videos/457290_Focks_South Africa_1920x1080.mp4', caption: 'Welcome to South Africa' }
    ];

    const videoElement = document.getElementById('video-slider');
    const captionElement = document.querySelector('.content p');

    if (videoElement && captionElement) {
        let currentIndex = 0;

        function changeVideo() {
            if (videoSources.length === 0) return;
            const video = videoSources[currentIndex];
            videoElement.src = video.src;
            captionElement.textContent = video.caption;
            videoElement.load();
            videoElement.play();
            currentIndex = (currentIndex + 1) % videoSources.length;
        }

        // Set the interval to change video every 10 seconds
        setInterval(changeVideo, 5000);

        // Initial call to set the first video and caption
        changeVideo();
    } else {
        console.error('Video or caption element not found');
    }

    // rate us section
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
    

