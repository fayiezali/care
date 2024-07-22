# Generated by Django 5.0.6 on 2024-06-01 19:21

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
            name='CategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryField_name', models.CharField(max_length=150, verbose_name='Category Name')),
                ('categoryField_slug', models.SlugField(max_length=150, unique=True, verbose_name='Category Slug')),
                ('categoryField_image', models.ImageField(default='Default_Image.png', upload_to='Category_File_Photo/', verbose_name='Image Preview')),
                ('categoryField_available', models.BooleanField(default=True, verbose_name='Available')),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
                'ordering': ('categoryField_name',),
            },
        ),
        migrations.CreateModel(
            name='CouponModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CouponField_code', models.CharField(max_length=50)),
                ('CouponField_discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('CouponField_valid_from', models.DateTimeField()),
                ('CouponField_valid_to', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CustomerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerField_mobile', models.CharField(max_length=20, verbose_name='Mobile Number ')),
                ('customerField_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Full Name ')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
                'ordering': ('customerField_user', 'customerField_mobile'),
            },
        ),
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderField_status', models.CharField(choices=[('New', 'New'), ('Pending', 'Pending'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='New', max_length=20)),
                ('orderField_date', models.DateTimeField(auto_now_add=True)),
                ('orderField_is_finished', models.BooleanField(default=False)),
                ('orderField_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.customermodel')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'ordering': ('-orderField_date', 'orderField_customer'),
            },
        ),
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productField_name', models.CharField(max_length=200)),
                ('productField_price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('productField_stock', models.PositiveIntegerField(default=0)),
                ('productField_description', models.TextField()),
                ('productField_image', models.ImageField(upload_to='Products_File_Photo/')),
                ('productField_availability', models.BooleanField(default=False)),
                ('productField_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.categorymodel')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ('productField_name',),
            },
        ),
        migrations.CreateModel(
            name='OrderDetailModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDetailField_quantity', models.IntegerField()),
                ('OrderDetailField_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('OrderDetailField_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.ordermodel')),
                ('OrderDetailField_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.productmodel')),
            ],
        ),
        migrations.CreateModel(
            name='RefundModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refundField_reason', models.TextField()),
                ('refundField_approved', models.BooleanField(default=False)),
                ('refundField_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.ordermodel')),
            ],
        ),
        migrations.CreateModel(
            name='ReviewModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReviewField_rating', models.IntegerField()),
                ('ReviewField_comment', models.TextField()),
                ('ReviewField_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.customermodel')),
                ('ReviewField_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.productmodel')),
            ],
        ),
    ]