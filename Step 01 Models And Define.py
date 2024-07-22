from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.utils.timezone import now


class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.get(pk=pk)
        obj.delete()

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Products(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.get(pk=pk)
        obj.delete()

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.get(pk=pk)
        obj.delete()

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.get(pk=pk)
        obj.delete()

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Coupon(models.Model):
    code = models.CharField(max_length=50)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.get(pk=pk)
        obj.delete()

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.get(pk=pk)
        obj.delete()

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    reason = models.TextField()
    approved = models.BooleanField(default=False)

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.get(pk=pk)
        obj.delete()

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.get(pk=pk)
        obj.delete()

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)
