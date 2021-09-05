from django.db import models


class FoodStore(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.TextField()
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.CharField(max_length=2, null=True )
    price = models.CharField(max_length=2, null=True)
    store = models.ForeignKey(FoodStore , on_delete=models.CASCADE)
    def __str__(self):
        return self.name

