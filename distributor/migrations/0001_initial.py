# Generated by Django 5.1.1 on 2024-11-20 14:51

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SalesRepresentative',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=18, validators=[django.core.validators.RegexValidator('^(\\+?\\d{0,2})?[\\D]?\\(?(\\d{3})\\)?[\\D]?(\\d{3})[\\D]?(\\d{4})$')])),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=18, validators=[django.core.validators.RegexValidator('^(\\+?\\d{0,2})?[\\D]?\\(?(\\d{3})\\)?[\\D]?(\\d{3})[\\D]?(\\d{4})$')])),
                ('order_dates', models.CharField(blank=True, max_length=25)),
                ('sales_reps', models.ManyToManyField(blank=True, to='distributor.salesrepresentative')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
