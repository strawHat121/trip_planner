# Generated by Django 4.1.5 on 2023-02-06 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0008_cities_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cities',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='http://127.0.0.1:8000/media/city/'),
        ),
    ]