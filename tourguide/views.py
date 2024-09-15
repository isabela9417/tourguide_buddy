from django.shortcuts import render
from .models import Video, MostVisitedSite

def home(request):
    videos = Video.objects.all()
    return render(request, 'home.html', {'videos': videos})


def gallery(request):
    most_visited_sites = MostVisitedSite.objects.all()
    return render(request, 'home.html', {'most_visited_sites': most_visited_sites})
