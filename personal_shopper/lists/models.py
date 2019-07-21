from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    address = models.TextField()


class Source(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    weight = models.FloatField()
    item_source = models.ForeignKey(Source, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
