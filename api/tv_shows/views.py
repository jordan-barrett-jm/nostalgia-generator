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
        
class ShowListByCategory(APIView):
    """
    List shows based on category
    """
    def post(self, request, format=None):
        req_serializer = RequestSerializer(data=request.data)
        if req_serializer.is_valid():
            shows = Show.objects.filter(category=req_serializer.data["category"])
            serializer = ShowSerializer(shows, many=True)
            return Response(serializer.data)
        return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class ShowLinkByCategory(APIView):
    """
    Return a video link from random TV show that matches specified category
    """
    def post (self, request, format=None):
        req_serializer = RequestSerializer(data=request.data)
        if req_serializer.is_valid():
            shows = Show.objects.filter(category=req_serializer.data["category"])
            random_index = random.randint(0, len(shows))
            print (shows)
            name = shows[random_index].name
            year = shows[random_index].start_year
            query = "%s %d" % (name, year)
            video_link = getVideoLink(query)
            serializer = VideoResponseSerializer(data = {"link": video_link})
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
