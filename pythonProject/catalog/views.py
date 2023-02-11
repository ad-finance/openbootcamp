from django.shortcuts import render
from .models import Director, Film, FilmInstance, DirectorInfo, Genre

def index(request):
    num_directors = Director.objects.all().count()
    num_films = Film.objects.all().count()
    num_instances = FilmInstance.objects.all().count()
    num_directorInfo = DirectorInfo.objects.all().count()

    return render(
        request,
        'index.html',
        context={
            'num_directors': num_directors,
            'num_films': num_films,
            'num_instances': num_instances,
            'num_directorInfo': DirectorInfo
        }
    )

