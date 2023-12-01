from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MaterialCardSerializer
from .models import MaterialCard

# Create your views here.

class MaterialCardView(viewsets.ModelViewSet):
    serializer_class = MaterialCardSerializer
    queryset = MaterialCard.objects.all()