"Graphene Schema"
import graphene
from graphene_django.types import DjangoObjectType
from api.tv_shows.models import Show
from api.tv_shows.video_search import getVideoLink

class ShowType(DjangoObjectType):
    video_link = graphene.String()
    class Meta:
        model = Show
        fields = ('name', 'category', 'start_year', 'end_year')
    
    def resolve_video_link(parent, info):
        return getVideoLink(f"{parent.name} {parent.start_year}")


class Query(object):
    all_shows = graphene.List(ShowType)

    def resolve_all_shows(self, info, **kwargs):
        return Show.objects.all()
