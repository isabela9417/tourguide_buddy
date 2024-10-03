from django.contrib import admin
from .models import Province, TourismSite, Video, MostVisitedSite

# Register your models here.
admin.site.register(Province)
admin.site.register(TourismSite)
admin.site.register(Video)
admin.site.register(MostVisitedSite)