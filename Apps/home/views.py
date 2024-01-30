from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import HomeSerializer
from .models import Home
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.


class HomeList(generics.ListAPIView):
    queryset = Home.objects.order_by('-created_at')
    serializer_class = HomeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['tag']
    search_fields = ['price','address', 'state']

class HomeDetail(generics.RetrieveAPIView):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
