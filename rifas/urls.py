from django.urls import path
from .views import criar_numeros, lista_rifa

urlpatterns = [
    path('criar_numeros/', criar_numeros, name='criar_numeros'),
    path('', lista_rifa, name='lista_rifa'),  # /rifas/
]
