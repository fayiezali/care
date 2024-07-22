# Generated by Django 5.0.6 on 2024-05-18 19:36

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
            name='ModelCoupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_code', models.CharField(max_length=50, unique=True)),
                ('coupon_valid_from', models.DateTimeField()),
                ('coupon_valid_to', models.DateTimeField()),
                ('coupon_discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('coupon_amount', models.FloatField()),
                ('coupon_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Coupon',
                'verbose_name_plural': 'Coupons',
                'ordering': ['-coupon_valid_to'],
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
                ('order_number', models.CharField(max_length=200)),
                ('order_total_amount', models.PositiveIntegerField(default=0)),
                ('order_is_finished', models.BooleanField(default=False)),
                ('order_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.modelcustomer')),
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
                ('product_image', models.ImageField(upload_to='products_File_Photo/')),
                ('product_availability', models.BooleanField(default=False)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.modelcategory')),
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
                ('cart_image', models.ImageField(upload_to='Cart_File_Photo/')),
                ('cart_order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.modelorder')),
                ('cart_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.modelproduct')),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
                'ordering': ('-cart_product',),
            },
        ),
        migrations.CreateModel(
            name='ModelRefund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refund_reason', models.TextField()),
                ('refund_processed', models.BooleanField(default=False)),
                ('refund_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.modelorder')),
            ],
            options={
                'verbose_name': 'Refund',
                'verbose_name_plural': 'Refunds',
                'ordering': ['-refund_order'],
            },
        ),
        migrations.CreateModel(
            name='ModelReviewsAndRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_rating', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], default='1', max_length=2)),
                ('review_comment', models.TextField()),
                ('review_created_at', models.DateTimeField(auto_now_add=True)),
                ('review_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.modelcustomer')),
                ('review_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.modelproduct')),
            ],
            options={
                'verbose_name': 'Reviews and Rating',
                'verbose_name_plural': 'Reviews and Rating',
                'ordering': ['-review_product'],
            },
        ),
    ]
