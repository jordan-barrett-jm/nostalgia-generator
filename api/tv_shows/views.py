from django.shortcuts import render
from tv_shows.serializers import ShowSerializer, RequestSerializer, VideoResponseSerializer
from tv_shows.models import Show
from tv_shows.video_search import getVideoLink
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import random


class ShowList(APIView):
    """
    List or add shows
    """
    def get(self, request, format=None):
        shows = Show.objects.all()
        serializer = ShowSerializer(shows, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ShowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
