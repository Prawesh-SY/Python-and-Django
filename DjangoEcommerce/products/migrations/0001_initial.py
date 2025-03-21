# Generated by Django 5.1.5 on 2025-02-14 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Price')),
                ('updated_price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Updated Price')),
                ('stock', models.PositiveIntegerField(verbose_name='Units in Stock')),
                ('expiry_date', models.DateField(verbose_name='Expiry Date')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is Available')),
                ('image', models.ImageField(upload_to='product/images', verbose_name='Upload Prodcut Image')),
                ('category', models.CharField(choices=[('PC', 'PC'), ('Clothes', 'Clothes')], max_length=50, verbose_name='Category')),
                ('made_in', models.CharField(max_length=50, verbose_name='Country of Origin')),
                ('brand', models.CharField(max_length=50, verbose_name='Brand')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Productasperhtml',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('des', models.TextField(verbose_name='Description')),
                ('category', models.CharField(max_length=111, verbose_name='Category')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price')),
                ('stock', models.PositiveIntegerField(verbose_name='Units In Stock')),
                ('image', models.ImageField(upload_to='product/images', verbose_name='Product Image')),
            ],
        ),
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
            ],
            options={
                'verbose_name': 'Cloth',
                'verbose_name_plural': 'Clothes',
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='PC',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.product')),
                ('usb_count', models.PositiveIntegerField(verbose_name='Total USB Ports')),
                ('special_features', models.TextField(max_length=240, verbose_name='Special Features')),
                ('cellular_tech', models.CharField(max_length=50, verbose_name='Cellular Technology')),
                ('memory_type', models.CharField(max_length=50, verbose_name='MEMORY type')),
                ('memory_size', models.CharField(max_length=50, verbose_name='MEMORY size')),
                ('graphics_type', models.CharField(max_length=50, verbose_name='Graphics Description')),
                ('graphics_memory', models.CharField(max_length=50, verbose_name='Dedicated Graphics Memory')),
                ('graphics_interface', models.CharField(max_length=100, verbose_name='Graphics Card Interface')),
                ('vid_op_interface', models.CharField(max_length=50, verbose_name='Video Output Interface')),
                ('vid_op_count', models.PositiveIntegerField(verbose_name='Total Video Output Ports')),
                ('wirless_tech', models.TextField(verbose_name='Wireless Communication Standards')),
                ('input_interface', models.TextField(verbose_name='Human Input Interface')),
                ('screen_size', models.PositiveIntegerField(verbose_name='Screen Size(in inches)')),
                ('components', models.TextField(verbose_name='Included Components')),
                ('operating_system', models.CharField(max_length=150, verbose_name='Operating System')),
                ('cpu_count', models.PositiveIntegerField(verbose_name='Processor Count')),
                ('cpu_type', models.CharField(max_length=100, verbose_name='Processor Type')),
                ('cpu_series', models.CharField(max_length=50, verbose_name='Processor Series')),
                ('cpu_clock', models.CharField(max_length=50, verbose_name='Processor Speed')),
                ('cpu_socket', models.CharField(max_length=50, verbose_name='CPU Socket')),
                ('resolution', models.CharField(max_length=50, verbose_name='Resolution')),
                ('connectivity', models.TextField(verbose_name='Connectivity Technology')),
                ('use_case', models.TextField(verbose_name='Specific Uses of Product')),
                ('storage_type', models.CharField(max_length=50, verbose_name='Storage type')),
                ('storage_size', models.CharField(max_length=50, verbose_name='Storage size')),
                ('color', models.CharField(max_length=50, verbose_name='Color')),
            ],
            options={
                'verbose_name': 'PC',
                'verbose_name_plural': 'PCs',
            },
            bases=('products.product',),
        ),
        migrations.CreateModel(
            name='Men',
            fields=[
                ('clothes_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.clothes')),
                ('type', models.CharField(choices=[('Topwear', 'Topwear'), ('Bottomwear', 'Bottomwear'), ('Footwear', 'Footwear'), ('Sports & Active wear', 'Sports & Active wear'), ('Fashion Accessories', 'Fashion Accessories'), ('Ethnic & Festive wear', 'Ethnic & Festive wear'), ('Innerwear & Sleepwear', 'Innerwear & Sleepwear'), ('Personal Care & Grooming', 'Personal Care & Grooming'), ('Sunglasses & Frames', 'Sunglasses & Frames'), ('Watches', 'Watches'), ('Gadgets', 'Gadgets'), ('Bags & Backpacks', 'Bags & Backpacks'), ('Luggages & Trolleys', 'Luggages & Trolleys')], max_length=50, verbose_name='Type')),
                ('size', models.CharField(max_length=50, verbose_name='Size')),
                ('fitting', models.CharField(max_length=50, verbose_name='Body Fitting')),
            ],
            bases=('products.clothes',),
        ),
    ]
