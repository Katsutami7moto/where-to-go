# Generated by Django 4.1.5 on 2023-01-31 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_remove_place_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
