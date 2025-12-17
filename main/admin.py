from django.contrib import admin
from .models import Shop

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'is_active', 'price', 'created_at']
    search_fields = ('name', 'description')
    list_filter = ['is_active', 'created_at']
