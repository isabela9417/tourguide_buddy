from django.shortcuts import render, get_object_or_404
from .models import Video, MostVisitedSite, Province, TourismSite
from django.urls import path
import requests
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


# query the provonces
def province_tourism_sites(request, province_name):
    
    province_name = province_name.replace('-', ' ')
    province = get_object_or_404(Province, name=province_name)
    tourism_sites = TourismSite.objects.filter(province=province)

    return render(request, 'province_tourism_sites.html', {
        'province': province,
        'tourism_sites': tourism_sites
    })