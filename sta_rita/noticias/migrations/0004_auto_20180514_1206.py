# Generated by Django 2.0.5 on 2018-05-14 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_auto_20180514_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='data',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
