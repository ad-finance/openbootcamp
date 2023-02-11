import uuid

from django.db import models
from django.urls import reverse

class Director(models.Model):
    name = models.CharField(max_length=64, help_text='Nombre del director:')

    def __str__(self):
        return self.name

class Genre(models.Model):
    genre = models.CharField(max_length=64, help_text='Genero:')

class Film(models.Model):
    title = models.CharField(max_length=32)
    genre = models.ManyToManyField(Genre)
    sinopsis = models.TextField(max_length=300)
    awards_and_festivals = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film-detail', args=[str(self.id)])

class FilmInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='ID unico para esta pelicula')
    film = models.ForeignKey('Film', on_delete= models.SET_NULL, null=True)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True)
    due_back = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('film detail', args=[str(self.id)])

class DirectorInfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('film detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first.name)

