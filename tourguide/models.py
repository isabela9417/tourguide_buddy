from django.db import models


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