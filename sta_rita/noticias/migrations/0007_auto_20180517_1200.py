# Generated by Django 2.0.5 on 2018-05-17 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0006_auto_20180517_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
