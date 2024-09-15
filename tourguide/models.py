from django.db import models
from django.utils.translation import gettext_lazy as _

class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class MostVisitedSite(models.Model):
    name = models.CharField(max_length=255)
    province = models.ForeignKey('Province', on_delete=models.CASCADE)
    background_image = models.ImageField(upload_to='backgrounds/')
    description = models.TextField()

    def __str__(self):
        return self.name


# Province model
class Province(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capitalCity = models.TextField(max_length=100)
    description = models.TextField(max_length=350, default='', blank=True, null=True)
    image = models.ImageField(upload_to='provinces/')
    
    def __str__(self):
        return self.name

# Tourism sites model
class TourismSite(models.Model):
    name = models.CharField(max_length=200)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    site_type = models.CharField(max_length=100)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    description = models.TextField(max_length=350, default='', blank=True, null=True)
    image = models.ImageField(upload_to='tourism_sites/')
    booking_link = models.URLField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.name

# Hotel model
class Hotel(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='hotels/')
    description = models.TextField(max_length=350, default='', blank=True, null=True)
    booking_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

# Rental car model
class RentalCar(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    image = models.ImageField(upload_to='car_servicess/')
    description = models.TextField(max_length=350, default='', blank=True, null=True)
    booking_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

# Customer or user model
class User(models.Model):
    name = models.CharField(max_length=200)
    lastName = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.ForeignKey(Province, on_delete=models.CASCADE)
    password = models.TextField()
    
    def __str__(self):
        return self.name

# Reviews model
class Review(models.Model):
    RATING_CHOICES = [
        (1, _('1 - Poor')),
        (2, _('2 - Fair')),
        (3, _('3 - Good')),
        (4, _('4 - Very Good')),
        (5, _('5 - Excellent')),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tourism_site = models.ForeignKey('TourismSite', on_delete=models.CASCADE, blank=True, null=True)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, blank=True, null=True)
    rental_car = models.ForeignKey('RentalCar', on_delete=models.CASCADE, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    text = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.rating} stars"

# rating model
class Rating(models.Model):
    entity_type = models.CharField(max_length=20, choices=[
        ('tourism_site', _('Tourism Site')),
        ('hotel', _('Hotel')),
        ('rental_car', _('Rental Car')),
    ])
    entity_id = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=Review.RATING_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.get_entity_type_display()} {self.entity_id} - {self.rating} stars"
