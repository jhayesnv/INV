# Generated by Django 5.1.1 on 2024-12-20 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]