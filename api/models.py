from django.db import models

class Location(models.Model):
    locationName = models.CharField(max_length=100 , unique=True )

    def __str__(self) -> str:
        return self.locationName

class Item(models.Model):
    itemName = models.CharField(max_length=100 , unique= True )
    addDate = models.DateField()
    itemLocation = models.ForeignKey(Location , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.itemName