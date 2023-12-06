from django.shortcuts import render
from .models import Rating,Meal,User
from rest_framework import viewsets
from .serializers import MealSerializer,RatingSerializer,UserSerializer


class Mealviewset(viewsets.ModelViewSet):
    queryset=Meal.objects.all()
    serializer_class=MealSerializer


class Ratingviewset(viewsets.ModelViewSet):
    queryset=Rating.objects.all()
    serializer_class=RatingSerializer
