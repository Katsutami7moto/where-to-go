from django.contrib import admin
from places.models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description_short', 'description_long',)
    list_display = ('title',)
