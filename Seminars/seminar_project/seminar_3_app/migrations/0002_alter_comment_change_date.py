# Generated by Django 4.2.4 on 2023-09-13 11:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('seminar_3_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='change_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]