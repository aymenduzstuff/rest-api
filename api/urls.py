
from django.urls import path 
from .views import ItemList , itemDetail , LocationList , locationDetail

urlpatterns = [
    path('item/' , ItemList.as_view()),
    path('item/<int:pk>' , itemDetail.as_view()),
    path('location/' , LocationList.as_view()),
    path('location/<int:pk>' , locationDetail.as_view()),
    
]
