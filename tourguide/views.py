from django.shortcuts import render
from .models import Video, MostVisitedSite

def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})


def gallery(request):
    most_visited_sites = MostVisitedSite.objects.all()
    return render(request, 'home.html', {'most_visited_sites': most_visited_sites})


def search_places(query):
    api_key = settings.GOOGLE_PLACES_API_KEY
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    
    params = {
        'key': api_key,
        'query': query,
        'fields': 'name,formatted_address,formatted_phone_number,website,opening_hours,photos'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        results = response.json().get('results', [])
        return results
    except requests.RequestException as e:
        print(f"Error searching places: {e}")
        return []

def get_place_details(place_id):
    api_key = settings.GOOGLE_PLACES_API_KEY
    url = 'https://maps.googleapis.com/maps/api/place/details/json'
    
    params = {
        'key': api_key,
        'place_id': place_id,
        'fields': 'name,formatted_address,formatted_phone_number,website,opening_hours,photos'
    }
    
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        place_details = response.json().get('result', {})
        return place_details
    except requests.RequestException as e:
        print(f"Error getting place details: {e}")
        return {}

def search_pexels_images(query):
    api_key = settings.PEXELS_API_KEY
    url = 'https://api.pexels.com/v1/search'
    
    headers = {
        'Authorization': api_key
    }
    
    params = {
        'query': query,
        'per_page': 1  # Number of images to fetch
    }
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Will raise an HTTPError for bad responses
        results = response.json().get('photos', [])
        if results:
            return results[0].get('url', '')
        else:
            print(f"No images found for query: {query}")
            return ''  # No image found
    except requests.RequestException as e:
        print(f"Error searching Pexels images: {e}")
        return ''

def get_suggestions(request):
    if request.method == 'POST':
        query = request.POST.get('query', '')
        if not query:
            return render(request, 'home.html', {'error': 'Query cannot be empty'})

        # Search for places based on the query
        all_place_details = {}
        places = search_places(query)
        for place in places:
            place_id = place.get('place_id')
            if place_id:
                place_details = get_place_details(place_id)
                place_name = place_details.get('name', '')
                place_details['pexels_image'] = search_pexels_images(place_name)
                all_place_details[place_id] = place_details

        # Provide data to the template
        return render(request, 'results.html', {
            'query': query,
            'place_details': all_place_details
        })
    else:
        return render(request, 'home.html')

def search_results(request):
    query = request.POST.get('query', '')
    
    results = perform_search(query)
    return render(request, 'results.html', {'results': results})