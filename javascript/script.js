// The search button and search bar elements
let searchBtn = document.querySelector('#search-btn');
let searchBar = document.querySelector('.search-bar-container');

// The bar menu on small screens
let menu = document.querySelector('#menu-bar');
let navbar = document.querySelectorAll('.navbar');

// video slider
let videobtn = document.querySelector('.vid-btn');


document.addEventListener('DOMContentLoaded', () => {
    // The search button and search bar elements
    const searchBtn = document.querySelector('#search-btn');
    const searchBar = document.querySelector('.search-bar-container');
    
// menu bar on smaller screens
menu.addEventListener('click', () =>{
    menu.classList.toggle('bx-x');
    navbar.classList.toggle('active');
});


window.onscroll = () =>{
    menu.classList.remove('bx-x');
    navbar.classList.remove('active');
}

// videobtn.forEach(btn =>{
//     btn.addEventLister('click', () =>{
//         document.querySelector('.controls .active').classList.remove('active');
//         btn.classList.add('active');
//         let src = btn.getAttribute('data-src');
//         document.querySelector('#video-slider').src = src;
//     });
// });


    // Array of video sources
    const videoSources = [
        { src: 'videos/457446_South Africa_Africa_1920x1080.mp4', caption: 'Search for your destination, as it awaits you...' },
        { src: 'videos/463049_Elephant_Elephants_1920x1080.mp4', caption: 'Majestic elephants roaming free' },
        { src: 'videos/6013749_Nature_Forest_3840x2160.mp4', caption: 'Enchanting forest landscapes' },
        { src: 'videos/1112734_Windy_Roast_3840x2160.mp4', caption: 'Camping site, where family and friends time matters...' },
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
        setInterval(changeVideo, 10000);

        // Initial call to set the first video and caption
        changeVideo();
    } else {
        console.error('Video or caption element not found');
    }

    // Handling search button toggle
    searchBtn.addEventListener('click', () => {
        searchBtn.classList.toggle('bx-x');
        searchBar.classList.toggle('active');
    });

    // Handling menu bar toggle for small screens
    const menu = document.querySelector('#menu-bar');
    const navbar = document.querySelector('.navbar');

    menu.addEventListener('click', () => {
        menu.classList.toggle('bx-x');
        navbar.classList.toggle('active');
    });

    // Removing active classes on scroll
    window.onscroll = () => {
        menu.classList.remove('bx-x');
        navbar.classList.remove('active');
    };
});
