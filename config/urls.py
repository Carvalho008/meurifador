from django.contrib import admin
from django.urls import path, include
from rifas.views import home  # importe a view home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # raiz do site -> página inicial
    path('rifas/', include('rifas.urls')),
]
