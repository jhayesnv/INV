# Generated by Django 5.1.1 on 2024-11-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0005_beerorderitem_is_available_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='spiritorderitem',
            name='is_one_ounce_pour',
            field=models.BooleanField(default=False),
        ),
    ]
