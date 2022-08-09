from django.urls import path
from sneakers.views import add_Jordans, list_Jordans,add_Air_Force,list_Air_Force,add_Accessories,list_Accessories,search_products, search_products_Air_Force


urlpatterns = [
    path('list_Jordans/', list_Jordans, name='list_Jordans'),
    path('add_Jordans/', add_Jordans, name='add_Jordans'),
    path('list_Air_Force/', list_Air_Force, name='list_Air_Force'),
    path('add_Air_Force/', add_Air_Force, name='add_Air_Force'),
      path('list_Accessories/', list_Accessories, name='list_Accessories'),
    path('add_Accessories/', add_Accessories, name='add_Accessories'),




    path('search_products/', search_products, name='search_products'),
    path('search_products_Air_Force/', search_products_Air_Force, name='search_products'),

   
]