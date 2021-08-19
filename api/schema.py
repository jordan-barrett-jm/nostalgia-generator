import graphene

import tv_shows.schema

class Query(tv_shows.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)