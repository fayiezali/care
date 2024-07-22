# Generated by Django 5.0.6 on 2024-05-13 15:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
                ('category_slug', models.SlugField(max_length=200, unique=True)),
                ('category_image', models.ImageField(db_index=True, default='Default_Image.png', upload_to='Catgory_File_Photo/', verbose_name='Image Preview')),
                ('category_availability', models.BooleanField(db_index=True, default=False, verbose_name='Available')),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='ModelCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_mobile', models.CharField(max_length=20)),
                ('customer_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ('customer_user',),
            },
        ),
        migrations.CreateModel(
            name='ModelOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('New', 'New'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='New', max_length=20)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('order_transaction_id', models.CharField(max_length=200)),
                ('order_is_finished', models.BooleanField(default=False)),
                ('order_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.modelcustomer')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('-order_date', 'order_customer'),
            },
        ),
        migrations.CreateModel(
            name='ModelProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_slug', models.SlugField(max_length=200, unique=True)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_stock', models.PositiveIntegerField(default=0)),
                ('product_description', models.TextField()),
                ('product_image', models.ImageField(upload_to='products/')),
                ('product_availability', models.BooleanField(default=False)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.modelcategory')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Producs',
                'ordering': ('product_name',),
            },
        ),
        migrations.CreateModel(
            name='ModelCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_quantity', models.PositiveIntegerField(default=0)),
                ('cart_price', models.PositiveIntegerField(default=0)),
                ('cart_creation_date', models.DateTimeField(auto_now_add=True)),
                ('cart_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.modelorder')),
                ('cart_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.modelproduct')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
                'ordering': ('-cart_product',),
            },
        ),
    ]