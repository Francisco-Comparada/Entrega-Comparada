from operator import index
from django.contrib import admin
from django.urls import path,include
from Entrega_Comparada.views import index, shop


urlpatterns = [
    path('admin/', admin.site.urls),
      path('',index),
    path('index/',index),
    path('shop/',shop),
    
    path('sneakers/', include('sneakers.urls'))
]
