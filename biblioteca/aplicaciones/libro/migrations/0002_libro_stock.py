# Generated by Django 4.2 on 2023-05-05 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='stock',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]
