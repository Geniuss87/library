from django.contrib import admin

from book.models import Book, Genre, Picture

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Picture)

