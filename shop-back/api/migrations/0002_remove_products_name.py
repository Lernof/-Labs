# Generated by Django 4.1.5 on 2023-01-14 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='name',
        ),
    ]
