# Generated by Django 4.2 on 2023-05-04 03:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoriaLibro', to='libro.categoria'),
        ),
    ]
