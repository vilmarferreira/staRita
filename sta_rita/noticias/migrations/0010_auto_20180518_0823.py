# Generated by Django 2.0.5 on 2018-05-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0009_auto_20180517_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]