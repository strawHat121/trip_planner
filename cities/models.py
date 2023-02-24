from django.db import models
from django.conf import settings

class Cities(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='city/',blank=True,null=True)
    def __str__(self):
        return self.name


class UserForm(models.Model):
    """User Object."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    name = models.CharField(max_length=255)
    start_date = models.DateField()
    travel_days = models.IntegerField()
    free_times = models.CharField(max_length=255)
    budget = models.CharField(max_length=255)
    travel_with = models.JSONField()
    interests = models.JSONField()
    partial_filter_query = models.JSONField(null=True, blank=True)
    full_filter_query = models.JSONField(null=True, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.user.email

class Places(models.Model):
    """Places to show in Cities"""
    city_name = models.ForeignKey(Cities, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    reviews = models.IntegerField()
    open_close_time = models.JSONField()
    spend_time = models.IntegerField()
    matched = models.IntegerField()
    travel_with = models.JSONField()
    budget = models.CharField(max_length=255)
    interest = models.JSONField()
    
    def __str__(self):
        return self.name


class PlaceImages(models.Model):
    place = models.ForeignKey(Places,on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='places/',null=True, blank=True)

    def __str__(self):
        return str(self.place)
