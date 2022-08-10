# Admin packages
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin

# Models
from book.models import Book, Genre


@admin.register(Book)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('title', 'location')


admin.site.register(Genre)