"""
Serializers for cities API
"""

from rest_framework import serializers
from .models import UserForm,Cities, Places, PlaceImages


class UserFormSerializer(serializers.ModelSerializer):
    """Serializer for City."""
    
    class Meta:
        model = UserForm
        fields = '__all__'
        read_only_fields = ['id','user','city']

class CitySerializer(serializers.ModelSerializer):
    """Serializer for City."""
    
    class Meta:
        model = Cities
        fields = '__all__'
        read_only_fields = ['id']

class PlaceImageSerializer(serializers.ModelSerializer):
    image = serializers.ListField(
        child=serializers.ImageField(max_length=10000,use_url=True))
    class Meta:
        model = PlaceImages
        fields = '__all__'
    
    def create(self,validated_data):
        place =validated_data['place']
        image = validated_data.pop('image')
        img_list = []
        for img in image:
            photo = PlaceImages.objects.create(place=place,image=img)
            photourl = f'{photo.image.url}'
            img_list.append(photourl)
        return img_list


class PlaceImageViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImages
        fields = '__all__'

class PlacesSerializer(serializers.ModelSerializer):
    """Serializer for places"""
    
    class Meta:
        model = Places
        fields = '__all__'
        read_only_fields = ['id','city_name']
    
