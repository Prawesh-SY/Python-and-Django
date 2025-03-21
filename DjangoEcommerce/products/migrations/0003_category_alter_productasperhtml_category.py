# Generated by Django 5.1.5 on 2025-02-18 09:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_productasperhtml_units_sold_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=111, verbose_name='Category')),
            ],
        ),
        migrations.AlterField(
            model_name='productasperhtml',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.category', verbose_name='Category'),
        ),
    ]
