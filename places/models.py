from django.db import models

# Create your models here.

class Place(models.Model):
    title = models.CharField('Название', max_length=200)
    description_short = models.TextField('Краткое описание')
    description_long = models.TextField('Полное описание')
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    index_number = models.IntegerField(null=True)
    image = models.ImageField(upload_to='img', null=True)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images')

    def __str__(self):
        return f'{self.place} - {self.index_number}'
