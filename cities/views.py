"""Views for cities API"""

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import generics
from django.db.models import Q
from .models import UserForm,Cities,Places, PlaceImages
from .serializers import UserFormSerializer,CitySerializer, PlacesSerializer, PlaceImageSerializer

class UserFormAPIView(APIView):
    serializer_class = UserFormSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        form = UserForm.objects.filter(user=self.request.user)
        serializer = UserFormSerializer(form, many=True)
        return Response({"form":serializer.data})
    
    def post(self,request):
        serializer = self.serializer_class(data=request.data,context={"request":request})
        if serializer.is_valid():
            """Assigning a userform to a city"""
            name = serializer.validated_data.get('name')
            budget = serializer.validated_data.get('budget')
            queryset = Cities.objects.filter(name=name)
            object = get_object_or_404(queryset)
            """Filtering the response according to the user form"""
            partial_filter_query = []
            city_filter_query= list(Places.objects.filter(city_name__name=name).values())
            places_image_filter_query = Places.objects.filter(city_name__name=name).values()
            partial_filter_query.append(city_filter_query)
            for place_name in places_image_filter_query:
                partial_filter_query.append(list(PlaceImages.objects.filter(place__name=place_name['name']).values('id','place_id','image')))
            #print(Places.objects.filter(city_name__name=name, budget=budget))
            """Getting full response"""
            full_filter_query = serializer.validated_data.get('full_filter_query')
            """saving the data"""
            serializer.save(user=request.user,city_id=object.id,partial_filter_query=partial_filter_query,full_filter_query=full_filter_query)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CityAPIView(APIView):
    serializer_class = CitySerializer
    parser_classes = (MultiPartParser, FormParser)
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        city = Cities.objects.all()
        serializer = CitySerializer(city, many=True,context={"request":request})
        return Response({"city":serializer.data},status=status.HTTP_200_OK)


class PlacesAPIView(APIView):
    serializer_class = PlacesSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        place = Places.objects.all()
        serializer = PlacesSerializer(place,many=True)
        return Response({"place":serializer.data})


class PlaceImagesAPIView(generics.ListCreateAPIView):
    queryset = PlaceImages.objects.all()
    serializer_class = PlaceImageSerializer
    parser_classes = (MultiPartParser, FormParser)
    def post(self, request, format=None): 
        serializer = PlaceImageSerializer(data=request.data)
        if serializer.is_valid():    #validate the serialized data to make sure its valid       
            qs = serializer.save()                     
            message = {'detail':qs, 'status':True}
            return Response(message, status=status.HTTP_201_CREATED)
        else: #if the serialzed data is not valid, return erro response
            data = {"detail":serializer.errors, 'status':False}            
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
    def get_queryset(self):
        return PlaceImages.objects.all()

    
