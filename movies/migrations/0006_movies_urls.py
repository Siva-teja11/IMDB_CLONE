# Generated by Django 4.2.4 on 2023-12-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_alter_movies_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='urls',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
