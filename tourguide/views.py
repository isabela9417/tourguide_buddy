from django.shortcuts import render, get_object_or_404
from .models import Video, MostVisitedSite, Province, TourismSite
from django.urls import path
import requests
from django.core.mail import send_mail
from decouple import config
from django.conf import settings



def home(request):
    videos = Video.objects.all()
    most_visited_sites = MostVisitedSite.objects.all()
    return render(request, 'home.html', {'videos': videos,'most_visited_sites': most_visited_sites})


def get_suggestions(request):
    place_details = {}
    google_api_key = settings.GOOGLE_PLACES_API_KEY  # Use Google Places API key

    if request.method == "POST":
        selected_topic = request.POST.get("topic")

        if selected_topic:
            try:
                # Step 1: Fetch places using Google Places API
                response = requests.get(
                    f"https://maps.googleapis.com/maps/api/place/textsearch/json?query={selected_topic}&key={google_api_key}"
                )
                response.raise_for_status()  # Raise an error for bad responses
                place_suggestions = response.json().get('results', [])

                # Step 2: Fetch details for each place
                for place in place_suggestions:
                    place_id = place['place_id']
                    place_name = place['name']
                    formatted_address = place.get('formatted_address', 'N/A')

                    # Fetch detailed place information using Google Places API
                    details_response = requests.get(
                        f"https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&key={google_api_key}"
                    )
                    details_response.raise_for_status()  # Raise an error for bad responses
                    place_details_data = details_response.json().get('result', {})

                    # Extract additional details
                    formatted_phone_number = place_details_data.get('formatted_phone_number', 'N/A')
                    website = place_details_data.get('website', '#')

                    # Fetch photo references
                    photos = place_details_data.get('photos', [])
                    image_url = (
                        f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photos[0]['photo_reference']}&key={google_api_key}"
                        if photos else None
                    )

                    place_details[place_id] = {
                        'name': place_name,
                        'formatted_address': formatted_address,
                        'formatted_phone_number': formatted_phone_number,
                        'website': website,
                        'image_url': image_url  # Corrected variable name
                    }

                if not place_details:
                    answer = "No places found for the selected topic."
                    
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                answer = "Error fetching places from the API."

    return render(request, 'results.html', {'place_details': place_details})

# contact us section
def contact(request):
    success_message = None  # Initialize success message

    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        contact_number = request.POST['contact-number']
        subject = request.POST['subject']
        message = request.POST['message']

        # List of email recipients
        recipients = ['isabelachana@gmail.com', 'isabela.tlhakudi@gmail.com']

        # Send email
        send_mail(
            subject,
            f'Message from {name} ({contact_number}): {message}',
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )

        # Set the success message
        success_message = f"{name}, your contact has been sent successfully."

    # Render the contact section with the success message
    return render(request, 'home.html', {'success_message': success_message})


# query the provonces
def tourism_sites(request, province_name):
    province = get_object_or_404(Province, name=province_name)
    tourism_sites = TourismSite.objects.filter(province=province)  # Filter by province

    context = {
        'province': province,
        'tourism_sites': tourism_sites,
    }
    return render(request, 'tourism-sites.html', context)