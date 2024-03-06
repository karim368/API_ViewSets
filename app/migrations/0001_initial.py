# Generated by Django 5.0.2 on 2024-03-06 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('product_category_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('product_category_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.PositiveIntegerField()),
                ('product_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.productcategory')),
            ],
        ),
    ]
