# Generated by Django 2.0.5 on 2018-05-14 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missas', '0002_auto_20180514_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='missa',
            name='diaSemana',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
