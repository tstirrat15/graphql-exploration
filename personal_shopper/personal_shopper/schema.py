from graphene import Schema, ObjectType

from lists.schema import Query as ListsQuery


class Query(ListsQuery, ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = Schema(query=Query)
