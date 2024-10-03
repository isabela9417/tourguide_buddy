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

// Review slider
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

// Search and update results
document.addEventListener('DOMContentLoaded', () => {
    const searchBar = document.querySelector('#search-bar');
    const resultsSection = document.querySelector('#results');

    searchBar.addEventListener('input', function() {
        const query = this.value;
        if (query.length < 3) {
            resultsSection.innerHTML = '<p>Type at least 3 characters to search.</p>';
            return;
        }

        fetch("{% url 'get_suggestions' %}", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({ query })
        })
        .then(response => response.json())
        .then(data => {
            const placeDetails = data.place_details;
            let output = '';

            for (const [placeId, details] of Object.entries(placeDetails)) {
                const image = details.pexels_image ? `https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=${details.pexels_image}&key=YOUR_GOOGLE_PLACES_API_KEY` : '{% static 'images/placeholder.png' %}';
                const openingHours = details.opening_hours.open_now ? 'Open now' : 'Closed';

                output += `
                    <div class="box">
                        <img src="${image}" alt="Image of ${details.name}">
                        <div class="content">
                            <h3>${details.name}</h3>
                            <p><strong>Address:</strong> ${details.formatted_address}</p>
                            <p><strong>Phone:</strong> ${details.formatted_phone_number}</p>
                            <p><strong>Website:</strong> <a href="${details.website}" target="_blank">${details.website}</a></p>
                            <p><strong>Opening Hours:</strong> ${openingHours}</p>
                        </div>
                    </div>`;
            }

            resultsSection.innerHTML = output;
        })
        .catch(error => {
            resultsSection.innerHTML = '<p>Error retrieving results.</p>';
        });
    });
});

// Video autoplay functionality
document.addEventListener('DOMContentLoaded', () => {
    const videoSources = [
        {% for video in videos %}
            { src: "{{ video.video_file.url }}", caption: "{{ video.description }}" },
        {% endfor %}
    ];

    const videoElement = document.getElementById('video-slider');
    const captionElement = document.getElementById('caption');

    if (videoElement && captionElement) {
        let currentIndex = 0;

        function changeVideo() {
            if (videoSources.length === 0) return;
            const video = videoSources[currentIndex];
            
            // Update the video src directly
            videoElement.src = video.src;
            
            // Update the caption
            captionElement.textContent = video.caption;
            
            // Load and play the new video
            videoElement.load();
            videoElement.play();
            
            // Move to the next video, loop back if at the end
            currentIndex = (currentIndex + 1) % videoSources.length;
        }

        // Set the interval to change video every 5 seconds
        setInterval(changeVideo, 5000);

        // Initial call to set the first video and caption
        changeVideo();
    } else {
        console.error('Video or caption element not found');
    }
});
