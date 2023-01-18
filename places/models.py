from django.db import models

# Create your models here.

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')
    images = models.JSONField('Изображения')

    def __str__(self):
        return self.title
