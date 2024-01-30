from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.AddSellRequest.as_view(), name='sellrequest_add')
]
