from django.contrib import admin
from places.models import Place, Image

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description_short', 'description_long',)
    list_display = ('title',)

admin.site.register(Image)
