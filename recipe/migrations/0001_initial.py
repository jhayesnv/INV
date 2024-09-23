# Generated by Django 5.1.1 on 2024-09-23 00:54

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BarRecipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('instructions', models.TextField(blank=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('ingredients', models.ManyToManyField(to='inventory.foodorderitem')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CocktailRecipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('instructions', models.TextField(blank=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(choices=[('Beer-based', 'Beer-based'), ('Classic/Vintage', 'Classic/Vintage'), ('Contemporary Classic', 'Contemporary Classic'), ('Hot', 'Hot'), ('Levitate Menu', 'Levitate Menu'), ('Long Drinks/Highballs', 'Long Drinks/Highballs'), ('Martini', 'Martini'), ('Modern', 'Modern'), ('Molecular', 'Molecular'), ('Non-Alcoholic', 'Non-Alcoholic'), ('Punch', 'Punch'), ('Shots', 'Shots'), ('Sours', 'Sours'), ('Tiki/Tropical', 'Tiki/Tropical'), ('Wine-based', 'Wine-based')], default='Levitate Menu', max_length=21)),
                ('base_spirit', models.CharField(choices=[('Vodka', 'Vodka'), ('Gin', 'Gin'), ('Rum', 'Rum'), ('Tequila', 'Tequila'), ('Mezcal', 'Mezcal'), ('Brandy', 'Brandy'), ('Liqueur', 'Liqueur'), ('Bourbon', 'Bourbon'), ('Rye', 'Rye'), ('Scotch', 'Scotch'), ('Cachaca', 'Cachaca'), ('Genever', 'Genever'), ('Pisco', 'Pisco'), ('Other', 'Other'), ('Split', 'Split')], default='Bourbon', max_length=7)),
                ('method', models.CharField(choices=[('Shake/Strain', 'Shake/Strain'), ('Shake/Dump', 'Shake/Dump'), ('Stir/Strain', 'Stir/Strain'), ('Build', 'Build')], default='Shake/Strain', max_length=12)),
                ('glassware', models.CharField(blank=True, max_length=50)),
                ('garnish', models.CharField(blank=True, max_length=50)),
                ('bar_ingredients', models.ManyToManyField(to='recipe.barrecipe')),
                ('spirit_ingredients', models.ManyToManyField(to='inventory.spiritorderitem')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='KitchenRecipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('instructions', models.TextField(blank=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('is_gluten_free', models.BooleanField(default=False)),
                ('is_vegetarian', models.BooleanField(default=False)),
                ('ingredients', models.ManyToManyField(to='inventory.foodorderitem')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MenuItemRecipe',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('instructions', models.TextField(blank=True)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('is_brunch', models.BooleanField(default=False)),
                ('is_social_hour', models.BooleanField(default=False)),
                ('recipes', models.ManyToManyField(to='recipe.kitchenrecipe')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
