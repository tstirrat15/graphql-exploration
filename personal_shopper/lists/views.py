from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Client, Source, Item
from .serializers import ClientSerializer, SourceSerializer, ItemSerializer


class ClientViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True)
    def items(self, request, pk):
        items = Item.objects.filter(client__id=pk)
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)


class SourceViewset(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
