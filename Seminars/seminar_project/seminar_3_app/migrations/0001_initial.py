# Generated by Django 4.2.4 on 2023-09-05 11:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField(max_length=1000)),
                ('bd', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('post', models.TextField(max_length=1000)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('publish', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminar_3_app.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='seminar_3_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000)),
                ('publish_date', models.DateField(auto_now_add=True)),
                ('change_date', models.DateField(default=datetime.date(2023, 9, 5))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminar_3_app.author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seminar_3_app.post')),
            ],
        ),
    ]
