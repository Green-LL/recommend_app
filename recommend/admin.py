# recommend/admin.py
from django.contrib import admin
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'tags')
    list_filter = ('media_type',)
    search_fields = ('title', 'tags', 'reason')