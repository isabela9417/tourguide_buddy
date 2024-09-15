from django.contrib import admin
from .models import Province, TourismSite, Hotel, RentalCar, User, Review, Rating, Video, MostVisitedSite

# Register your models here.
admin.site.register(Province)
admin.site.register(TourismSite)
admin.site.register(Hotel)
admin.site.register(RentalCar)
admin.site.register(User)
admin.site.register(Review)
admin.site.register(Rating)
admin.site.register(Video)
admin.site.register(MostVisitedSite)