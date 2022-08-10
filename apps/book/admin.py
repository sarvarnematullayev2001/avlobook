from django.contrib import admin
from book.models import Book, Genre
from django.contrib.gis.admin import OSMGeoAdmin

# Register your models here.
@admin.register(Book)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('title', 'location')


admin.site.register(Genre)