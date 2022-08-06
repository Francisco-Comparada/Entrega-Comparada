from django.urls import path
from sneakers.views import add_Jordans, list_Jordans,add_Air_Force,list_Air_Force,search_products


urlpatterns = [
    path('list_Jordans/', list_Jordans, name='list_Jordans'),
    path('add_Jordans/', add_Jordans, name='add_Jordans'),
    path('list_Air_Force/', list_Air_Force, name='list_Air_Force'),
    path('add_Air_Force/', add_Air_Force, name='add_Air_Force'),
    path('search_products/', search_products, name='search_products')
   
]