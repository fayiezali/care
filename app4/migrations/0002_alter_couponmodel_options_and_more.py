# Generated by Django 5.0.6 on 2024-06-15 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='couponmodel',
            options={'ordering': ('-CouponField_code',), 'verbose_name': 'Coupon', 'verbose_name_plural': 'Coupon'},
        ),
        migrations.AlterModelOptions(
            name='orderdetailmodel',
            options={'ordering': ('-OrderDetailField_order',), 'verbose_name': 'Order Detail', 'verbose_name_plural': 'Order Detail'},
        ),
        migrations.AlterModelOptions(
            name='refundmodel',
            options={'ordering': ('-refundField_order',), 'verbose_name': 'Refund', 'verbose_name_plural': 'Refund'},
        ),
        migrations.AlterModelOptions(
            name='reviewmodel',
            options={'ordering': ('-ReviewField_rating', 'ReviewField_product', 'ReviewField_customer'), 'verbose_name': 'Review', 'verbose_name_plural': 'Review'},
        ),
        migrations.AlterField(
            model_name='orderdetailmodel',
            name='OrderDetailField_quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='productField_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app4.categorymodel', verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='reviewmodel',
            name='ReviewField_rating',
            field=models.PositiveIntegerField(),
        ),
    ]
