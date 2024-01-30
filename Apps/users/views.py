from django.shortcuts import render
from .models import User
from .mixins import CustomLoginRequriedMixin
from .serializers import UserSerializer, UserSignInSerializer, UserSignUpSerializer
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

class UserSignUp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

class UserSignIn(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignInSerializer

class UserCheckLogIn(CustomLoginRequriedMixin, generics.RetrieveAPIView):
    def get(self, request, *args, **kwargs):
        serializer = UserSerializer([request.login_user], many=True)
        return Response(serializer.data[0])
    
class UserList(CustomLoginRequriedMixin,generics.ListAPIView):
    queryset = User.objects.all()[:20]
    serializer_class = UserSerializer