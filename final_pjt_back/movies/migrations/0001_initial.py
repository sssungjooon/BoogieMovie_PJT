# Generated by Django 3.2.13 on 2022-11-22 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_path', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('vote_average', models.FloatField()),
                ('vote_count', models.IntegerField()),
                ('overview', models.CharField(max_length=200)),
                ('release_date', models.DateField()),
                ('poster_path', models.CharField(max_length=200)),
                ('video_path', models.CharField(max_length=200)),
                ('actors', models.ManyToManyField(related_name='movies', to='movies.Actor')),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.Genre')),
                ('keywords', models.ManyToManyField(related_name='movies', to='movies.Keyword')),
            ],
        ),
    ]
