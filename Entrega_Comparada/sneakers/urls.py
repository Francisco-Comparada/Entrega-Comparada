from django.urls import path
from sneakers.views import add_Jordans, list_Jordans,add_Air_Force,list_Air_Force,add_Accessories,list_Accessories,search_products,Shop_single_Jordans, Shop_single_Air_Force,Shop_single_Accessories


urlpatterns = [
    path('list_Jordans/', list_Jordans, name='list_Jordans'),
    path('add_Jordans/', add_Jordans, name='add_Jordans'),
    path('Shop_single_Jordans/<int:pk>/', Shop_single_Jordans, name='Shop_single_Jordans'),

    path('list_Air_Force/', list_Air_Force, name='list_Air_Force'),
    path('add_Air_Force/', add_Air_Force, name='add_Air_Force'),
    path('Shop_single_Air_Force/<int:pk>/', Shop_single_Air_Force, name='Shop_single_Air_Force'),


    path('list_Accessories/', list_Accessories, name='list_Accessories'),
    path('add_Accessories/', add_Accessories, name='add_Accessories'),
    path('Shop_single_Accessories/<int:pk>/', Shop_single_Accessories, name='Shop_single_Accessories'),




    path('search_products/', search_products, name='search_products'),
   
] 
