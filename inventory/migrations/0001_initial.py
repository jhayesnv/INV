# Generated by Django 5.1.1 on 2024-09-23 00:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('distributor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseRegion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('area', models.CharField(choices=[('Kitchen', 'Kitchen'), ('Bar', 'Bar'), ('Other', 'Other')], default='Kitchen', max_length=7)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Grape',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('color', models.CharField(choices=[('Red', 'Red'), ('White', 'White')], default='Red', max_length=5)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('category', models.CharField(choices=[('Wine', 'Wine'), ('Beer', 'Beer'), ('Spirits', 'Spirits'), ('Sake', 'Sake')], default='Spirits', max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('baseregion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.baseregion')),
                ('area', models.CharField(choices=[('Argentina', 'Argentina'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Barbados', 'Barbados'), ('Barbados', 'Barbados'), ('Belgium', 'Belgium'), ('Brazil', 'Brazil'), ('Bulgaria', 'Bulgaria'), ('Canada', 'Canada'), ('Caribbean', 'Caribbean'), ('Chile', 'Chile'), ('China', 'China'), ('Cuba', 'Cuba'), ('Czech Republic', 'Czech Republic'), ('Dominican Republic', 'Dominican Republic'), ('England', 'England'), ('France', 'France'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Greece', 'Greece'), ('Guadeloupe', 'Guadeloupe'), ('Guatemala', 'Guatemala'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Hungary', 'Hungary'), ('India', 'India'), ('Ireland', 'Ireland'), ('Israel', 'Israel'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Mauritius', 'Mauritius'), ('Martinique', 'Martinique'), ('Mexico', 'Mexico'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Puerto Rico', 'Puerto Rico'), ('Panama', 'Panama'), ('Philippines', 'Philippines'), ('Portugal', 'Portugal'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Saint Lucia', 'Saint Lucia'), ('Scotland', 'Scotland'), ('Slovenia', 'Slovenia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'), ('Switzerland', 'Switzerland'), ('Taiwan', 'Taiwan'), ('Thailand', 'Thailand'), ('Trinidad/Tobago', 'Trinidad/Tobago'), ('Turkey', 'Turkey'), ('United States', 'United States'), ('Venezuela', 'Venezuela'), ('Wales', 'Wales')], default='United States', max_length=18)),
            ],
            bases=('inventory.baseregion',),
        ),
        migrations.CreateModel(
            name='SubRegion',
            fields=[
                ('baseregion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.baseregion')),
            ],
            bases=('inventory.baseregion',),
        ),
        migrations.CreateModel(
            name='FoodOrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('par', models.DecimalField(decimal_places=1, default=1.0, max_digits=3)),
                ('quantity_on_hand', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('product_identifier', models.CharField(blank=True, max_length=64)),
                ('needs_ordering', models.BooleanField(default=False)),
                ('latest_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('unit', models.CharField(choices=[('cs', 'cs'), ('btl', 'btl'), ('box', 'box'), ('can', 'can'), ('bucket', 'bucket'), ('ea', 'ea'), ('flats', 'flats'), ('sticks', 'sticks'), ('#', '#'), ('lbs', 'lbs'), ('gal', 'gal'), ('oz', 'oz'), ('dz', 'dz'), ('as needed', 'as needed')], default='cs', max_length=9)),
                ('area_categories', models.ManyToManyField(to='inventory.category')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.distributor')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpiritOrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('par', models.DecimalField(decimal_places=1, default=1.0, max_digits=3)),
                ('quantity_on_hand', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('product_identifier', models.CharField(blank=True, max_length=64)),
                ('needs_ordering', models.BooleanField(default=False)),
                ('latest_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('unit', models.CharField(choices=[('cs', 'cs'), ('btl', 'btl')], default='btl', max_length=9)),
                ('category', models.CharField(choices=[('Vodka', 'Vodka'), ('Gin', 'Gin'), ('Rum', 'Rum'), ('Tequila', 'Tequila'), ('Mezcal', 'Mezcal'), ('Brandy', 'Brandy'), ('Liqueur', 'Liqueur'), ('Bourbon', 'Bourbon'), ('Rye', 'Rye'), ('Scotch', 'Scotch'), ('Cachaca', 'Cachaca'), ('Genever', 'Genever'), ('Pisco', 'Pisco'), ('Other', 'Other'), ('Split', 'Split')], default='Bourbon', max_length=7)),
                ('area_categories', models.ManyToManyField(to='inventory.category')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.distributor')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producer')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.region')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='producer',
            name='regions',
            field=models.ManyToManyField(to='inventory.region'),
        ),
        migrations.CreateModel(
            name='BeerOrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('par', models.DecimalField(decimal_places=1, default=1.0, max_digits=3)),
                ('quantity_on_hand', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('product_identifier', models.CharField(blank=True, max_length=64)),
                ('needs_ordering', models.BooleanField(default=False)),
                ('latest_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('unit', models.CharField(choices=[('keg', 'keg'), ('cans', 'cans'), ('btls', 'btls')], default='keg', max_length=9)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.distributor')),
                ('area_categories', models.ManyToManyField(to='inventory.category')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producer')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.region')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='region',
            name='sub_regions',
            field=models.ManyToManyField(to='inventory.subregion'),
        ),
        migrations.CreateModel(
            name='WineRegion',
            fields=[
                ('region_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.region')),
                ('geography', models.TextField(blank=True, help_text='country, area, natural features e.g. mountains, lakes, rivers, forests where in relation to other regions, etc.')),
                ('viticultural_techniques', models.TextField(blank=True, help_text='ripeness at harvest, vine training, harvest dates, irrigation, etc.')),
                ('vinification_techniques', models.TextField(blank=True, help_text='Fermentation, percentages of blends,  acidfication/must enrichments ,etc.')),
                ('aging_laws', models.TextField(blank=True, help_text='Oak, length of time in wood/btl, release dates, etc.')),
                ('offical_regional_classication', models.TextField(blank=True, help_text='VdT vs. AOP, etc.')),
                ('sub_regional_classifications', models.TextField(blank=True, help_text='Vineyards, villages, producers')),
                ('vintage_knowledge', models.TextField(blank=True, help_text='Poor/Fair/Good/Excellent - why')),
                ('law_terminology', models.TextField(blank=True, help_text='Gran Reserva vs. Crianza, etc.')),
                ('specific_terminology', models.TextField(blank=True, help_text='Aszu Essencia, Hanepoot, Sforzato, etc.')),
                ('grapes_allowed', models.ManyToManyField(to='inventory.grape')),
                ('major_producers', models.ManyToManyField(help_text='At least 5, what makes them unique, sig cuvees, historical lore', to='inventory.producer')),
            ],
            bases=('inventory.region',),
        ),
        migrations.CreateModel(
            name='WineOrderItem',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('par', models.DecimalField(decimal_places=1, default=1.0, max_digits=3)),
                ('quantity_on_hand', models.DecimalField(decimal_places=1, default=0.0, max_digits=3)),
                ('product_identifier', models.CharField(blank=True, max_length=64)),
                ('needs_ordering', models.BooleanField(default=False)),
                ('latest_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
                ('last_updated_at', models.DateTimeField(auto_now=True)),
                ('unit', models.CharField(choices=[('cs', 'cs'), ('btl', 'btl'), ('can', 'can')], default='cs', max_length=9)),
                ('vintage', models.CharField(blank=True, max_length=4)),
                ('style', models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Rose', 'Rose'), ('Sparkling', 'Sparkling'), ('Dessert', 'Dessert')], default='Red', max_length=9)),
                ('area_categories', models.ManyToManyField(to='inventory.category')),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='distributor.distributor')),
                ('grapes', models.ManyToManyField(to='inventory.grape')),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.producer')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.wineregion')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
    ]
