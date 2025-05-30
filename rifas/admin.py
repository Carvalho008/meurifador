from django.contrib import admin
from .models import NumeroRifa

@admin.register(NumeroRifa)
class NumeroRifaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nome', 'pago')
    list_filter = ('pago',)
    search_fields = ('numero', 'nome')
