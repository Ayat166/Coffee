# Generated by Django 4.1.1 on 2022-09-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='product_favorites',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
