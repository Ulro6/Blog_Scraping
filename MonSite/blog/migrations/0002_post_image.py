# Generated by Django 3.2.25 on 2024-03-22 14:54

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('C:/Users/quent/Blog_Scraping/MonSite/media')),
        ),
    ]
