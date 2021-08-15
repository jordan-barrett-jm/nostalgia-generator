from tv_shows.models import Show
from rest_framework import serializers

class ShowSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Show
        fields = ['name', 'category', 'start_year', 'end_year']