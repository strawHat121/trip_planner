# Generated by Django 4.1.5 on 2023-02-04 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0005_remove_cities_budget_remove_cities_free_times_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cities',
            name='user_form',
        ),
        migrations.AddField(
            model_name='userform',
            name='city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cities.cities'),
        ),
    ]
