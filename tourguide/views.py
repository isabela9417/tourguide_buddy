from django.shortcuts import render
from .models import Video, MostVisitedSite
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


# def search_pexels_images(query):
#     api_key = settings.PEXELS_API_KEY
#     url = 'https://api.pexels.com/v1/search'
    
#     headers = {
#         'Authorization': api_key
#     }
    
#     params = {
#         'query': query,
#         'per_page': 1  # Number of images to fetch
#     }
    
#     try:
#         response = requests.get(url, headers=headers, params=params)
#         response.raise_for_status()  # Will raise an HTTPError for bad responses
#         results = response.json().get('photos', [])
#         if results:
#             return results[0].get('src', {}).get('large', '')  # Adjust based on Pexels API response
#         else:
#             print(f"No images found for query: {query}")
#             return ''  # No image found
#     except requests.RequestException as e:
#         print(f"Error searching Pexels images: {e}")
#         return '' 



# def home(request):
#     videos = Video.objects.all()
#     most_visited_sites = MostVisitedSite.objects.all()
#     return render(request, 'home.html', {'videos': videos,'most_visited_sites': most_visited_sites})
    
# def search_places(query):
#     api_key = settings.GOOGLE_PLACES_API_KEY
#     url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    
#     params = {
#         'key': api_key,
#         'query': query,
#         'fields': 'name,formatted_address,formatted_phone_number,website,opening_hours,photos'
#     }
    
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()  # Will raise an HTTPError for bad responses
#         results = response.json().get('results', [])
#         return results
#     except requests.RequestException as e:
#         print(f"Error searching places: {e}")
#         return []

# def get_place_details(place_id):
#     api_key = settings.GOOGLE_PLACES_API_KEY
#     url = 'https://maps.googleapis.com/maps/api/place/details/json'
    
#     params = {
#         'key': api_key,
#         'place_id': place_id,
#         'fields': 'name,formatted_address,formatted_phone_number,website,opening_hours,photos'
#     }
    
#     try:
#         response = requests.get(url, params=params)
#         response.raise_for_status()  # Will raise an HTTPError for bad responses
#         place_details = response.json().get('result', {})
#         return place_details
#     except requests.RequestException as e:
#         print(f"Error getting place details: {e}")
#         return {}

# def get_suggestions(request):
#     if request.method == 'POST':
#         query = request.POST.get('query', '')
#         if not query:
#             return render(request, 'home.html', {'error': 'Query cannot be empty'})

#         # Search for places based on the query
#         all_place_details = {}
#         places = search_places(query)
#         for place in places:
#             place_id = place.get('place_id')
#             if place_id:
#                 place_details = get_place_details(place_id)
#                 place_name = place_details.get('name', '')
#                 place_details['pexels_image'] = search_pexels_images(place_name)
#                 all_place_details[place_id] = place_details

#         # Provide data to the template
#         return render(request, 'results.html', {
#             'query': query,
#             'place_details': all_place_details
#         })
#     else:
#         return render(request, 'home.html')

# def search_results(request):
#     query = request.POST.get('query', '')
#     results = perform_search(query)
#     return render(request, 'results.html', {'results': results})

# def search_pexels_images(query):
#     api_key = settings.PEXELS_API_KEY
#     url = 'https://api.pexels.com/v1/search'
    
#     headers = {
#         'Authorization': api_key
#     }
    
#     params = {
#         'query': query,
#         'per_page': 1  # Number of images to fetch
#     }
    
#     try:
#         response = requests.get(url, headers=headers, params=params)
#         response.raise_for_status()  # Will raise an HTTPError for bad responses
#         results = response.json().get('photos', [])
#         if results:
#             return results[0].get('url', '')
#         else:
#             print(f"No images found for query: {query}")
#             return ''  # No image found
#     except requests.RequestException as e:
#         print(f"Error searching Pexels images: {e}")
#         return ''
