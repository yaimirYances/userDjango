# Generated by Django 4.2 on 2023-05-05 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='seudonimo',
            field=models.CharField(blank=True, max_length=50, verbose_name='seudonimo'),
        ),
    ]
