# Generated by Django 4.1.5 on 2023-01-14 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_products_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
