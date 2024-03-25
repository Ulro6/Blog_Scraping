# Generated by Django 3.2.25 on 2024-03-25 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20240325_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Image'),
        ),
    ]
