"Graphene Schema"
import graphene
from graphene_django.types import DjangoObjectType
from tv_shows.models import Show
from tv_shows.video_search import getVideoLink
import random

class ShowType(DjangoObjectType):
    video_link = graphene.String()
    class Meta:
        model = Show
        fields = ('name', 'category', 'start_year', 'end_year')
    
    #generate the link to the video using the getVideoLink module and save that as an attribute of the ShowType
    def resolve_video_link(parent, info):
        return getVideoLink(f"{parent.name} {parent.start_year}")


class Query(object):
    all_shows = graphene.List(ShowType)
    show_by_name = graphene.Field(ShowType, name=graphene.String(required=True))
    random_show_by_category = graphene.Field(ShowType, category=graphene.String(required=True))

    def resolve_all_shows(self, info, **kwargs):
        return Show.objects.all()
    
    def resolve_show_by_name(self, info, name):
        return Show.objects.get(name=name)

    #return a random show in the list of shows that matches the specified category
    def resolve_random_show_by_category(self, info, category):
        shows = Show.objects.filter(category=category)
        show = shows[random.randint(0, len(shows))]
        return show