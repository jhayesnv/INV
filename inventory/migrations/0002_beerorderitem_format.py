# Generated by Django 5.1.1 on 2024-10-29 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='beerorderitem',
            name='format',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Can/Btl', 'Can/Btl')], default='Draft', max_length=7),
        ),
    ]
