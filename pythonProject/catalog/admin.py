from django.contrib import admin

from .models import Director, Film, FilmInstance, DirectorInfo, Genre

admin.site.register(Director)
admin.site.register(Film)
admin.site.register(FilmInstance)
admin.site.register(DirectorInfo)
admin.site.register(Genre)



