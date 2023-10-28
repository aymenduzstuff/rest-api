from rest_framework import generics 
from .models import Item , Location
from .serializers import itemSerializer , LocationSerializer

class ItemList(generics.ListCreateAPIView) :
    serializer_class = itemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')

        if location is not None :
            queryset = queryset.filter(itemLocation = location)

        return queryset
    
class itemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = itemSerializer 
    queryset = Item.objects.all()

    
class LocationList(generics.ListCreateAPIView):
    serializer_class = LocationSerializer 
    queryset = Location.objects.all()

    
class locationDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer 
    queryset = Location.objects.all()

