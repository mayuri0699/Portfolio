# Generated by Django 4.1.7 on 2023-07-03 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folioadmin', '0012_remove_aboutpage_status_alter_aboutpage_phone_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.TextField(blank=True, null=True)),
                ('instagram', models.TextField(blank=True, null=True)),
                ('whatsapp', models.TextField(blank=True, null=True)),
                ('linkdin', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
