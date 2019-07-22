from graphene import relay, ObjectType
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from .models import Item, Source, Client


class ItemNode(DjangoObjectType):
    class Meta:
        model = Item
        interfaces = (relay.Node, )
        filter_fields = '__all__'


class SourceNode(DjangoObjectType):
    class Meta:
        model = Source
        interfaces = (relay.Node, )
        filter_fields = '__all__'


class ClientNode(DjangoObjectType):
    class Meta:
        model = Client
        interfaces = (relay.Node, )
        filter_fields = '__all__'


class Query(ObjectType):
    item = relay.Node.Field(ItemNode)
    all_items = DjangoFilterConnectionField(ItemNode)

    source = relay.Node.Field(SourceNode)
    all_sources = DjangoFilterConnectionField(SourceNode)

    client = relay.Node.Field(ClientNode)
    all_clients = DjangoFilterConnectionField(ClientNode)
