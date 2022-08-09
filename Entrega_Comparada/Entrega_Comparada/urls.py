from operator import index
from django.contrib import admin
from django.urls import path,include
from Entrega_Comparada.views import index, shop

# para las imganes url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('',index),
    path('index/',index),
    path('shop/',shop),
    
    path('sneakers/', include('sneakers.urls')),#incluye todas las url que estan en sneakers
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)