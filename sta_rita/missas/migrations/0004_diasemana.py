# Generated by Django 2.0.5 on 2018-05-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('missas', '0003_missa_diasemana'),
    ]

    operations = [
        migrations.CreateModel(
            name='diaSemana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeDIa', models.CharField(max_length=100)),
            ],
        ),
    ]
