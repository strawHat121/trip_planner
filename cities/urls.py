from django.urls import path,include
from .views import UserFormAPIView,CityAPIView,PlacesAPIView, PlaceImagesAPIView



urlpatterns = [
    path('',CityAPIView.as_view()),
    path('form/',UserFormAPIView.as_view()),
    path('places/',PlacesAPIView.as_view()),
    path('places/image',PlaceImagesAPIView.as_view()),
]
