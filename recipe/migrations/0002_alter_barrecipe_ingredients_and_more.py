# Generated by Django 5.1.1 on 2024-11-17 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_beerorderitem_is_active_spiritorderitem_is_active_and_more'),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barrecipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='inventory.foodorderitem'),
        ),
        migrations.AlterField(
            model_name='cocktailrecipe',
            name='bar_ingredients',
            field=models.ManyToManyField(blank=True, to='recipe.barrecipe'),
        ),
        migrations.AlterField(
            model_name='cocktailrecipe',
            name='spirit_ingredients',
            field=models.ManyToManyField(blank=True, to='inventory.spiritorderitem'),
        ),
        migrations.AlterField(
            model_name='kitchenrecipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, to='inventory.foodorderitem'),
        ),
        migrations.AlterField(
            model_name='menuitemrecipe',
            name='recipes',
            field=models.ManyToManyField(blank=True, to='recipe.kitchenrecipe'),
        ),
    ]