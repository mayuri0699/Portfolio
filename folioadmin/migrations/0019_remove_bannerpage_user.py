# Generated by Django 4.1.7 on 2023-07-06 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folioadmin', '0018_bannerpage_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerpage',
            name='user',
        ),
    ]
