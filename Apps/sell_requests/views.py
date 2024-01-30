from django.shortcuts import render
from Apps.users.mixins import CustomLoginRequriedMixin
from rest_framework import generics
from .models import SellRequest
from .forms import SellRequestForm
from .serializers import SellRequestSerializer
from rest_framework.response import Response

# Create your views here.


class AddSellRequest(CustomLoginRequriedMixin, generics.CreateAPIView):
    queryset = SellRequest.objects.all()
    serializer_class = SellRequestSerializer

    def post(self, request, *args, **kwargs):
        request.data["user"] = request.login_user.id
        sellrequest_form = SellRequestForm(request.data)
        sellrequest = sellrequest_form.save()
        serializer = SellRequestSerializer([sellrequest], many=True)
        # many=True allows to serialiaze the list of objects instead of a single object
        return Response(serializer.data[0])
