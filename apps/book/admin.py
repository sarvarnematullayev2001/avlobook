# Admin packages
from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin

# Models
from book.models.book import Book, BookInstance
from book.models.genre import Genre


@admin.register(Book)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('title', 'location')


@admin.register(BookInstance)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('book', 'loan_status', 'due_by')


admin.site.register(Genre)