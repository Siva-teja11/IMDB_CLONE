# Generated by Django 4.2.4 on 2023-12-11 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='description',
            field=models.TextField(default='No description required'),
        ),
    ]
