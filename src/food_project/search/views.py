# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
#from search.models import Food
from . import serializers
from . import models
# Create your views here.

class FoodAPIView(generics.ListCreateAPIView):

    serializer_class = serializers.FoodSerializer
    queryset = models.Food.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'price')
