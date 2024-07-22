from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Categories(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, name, description=None):
        category = cls(name=name, description=description)
        category.save()
        return category

    @classmethod
    def read(cls, category_id):
        try:
            return cls.objects.get(id=category_id)
        except ObjectDoesNotExist:
            return None

    # The `update` method in each of the model classes (Categories, Products, Order, OrderDetails,
    # Coupon, Customer, Refund, Review) is a class method that allows updating the attributes of
    # an existing instance of that model.
    # The `update` method in each of the model classes (Categories, Products, Order, OrderDetails,
    # Coupon, Customer, Refund, Review) is a class method that allows updating the attributes of
    # an existing instance of that model.
    @classmethod
    def update(cls, category_id, **kwargs):
        category = cls.read(category_id)
        if category:
            for key, value in kwargs.items():
                setattr(category, key, value)
            category.save()
            return category
        return None

    @classmethod
    def delete(cls, category_id):
        category = cls.read(category_id)
        if category:
            category.delete()
            return True
        return False


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @classmethod
    def create(cls, category, name, description, price, stock, available=True):
        product = cls(category=category, name=name, description=description, price=price, stock=stock, available=available)
        product.save()
        return product

    @classmethod
    def read(cls, product_id):
        try:
            return cls.objects.get(id=product_id)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def update(cls, product_id, **kwargs):
        product = cls.read(product_id)
        if product:
            for key, value in kwargs.items():
                setattr(product, key, value)
            product.save()
            return product
        return None

    @classmethod
    def delete(cls, product_id):
        product = cls.read(product_id)
        if product:
            product.delete()
            return True
        return False


class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')])

    def __str__(self):
        return f'Order {self.id}'

    @classmethod
    def create(cls, customer, status='pending'):
        order = cls(customer=customer, status=status)
        order.save()
        return order

    @classmethod
    def read(cls, order_id):
        try:
            return cls.objects.get(id=order_id)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def update(cls, order_id, **kwargs):
        order = cls.read(order_id)
        if order:
            for key, value in kwargs.items():
                setattr(order, key, value)
            order.save()
            return order
        return None

    @classmethod
    def delete(cls, order_id):
        order = cls.read(order_id)
        if order:
            order.delete()
            return True
        return False


class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='order_details')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Order {self.order.id} - Product {self.product.name}'

    @classmethod
    def create(cls, order, product, quantity, price):
        order_detail = cls(order=order, product=product, quantity=quantity, price=price)
        order_detail.save()
        return order_detail

    @classmethod
    def read(cls, order_detail_id):
        try:
            return cls.objects.get(id=order_detail_id)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def update(cls, order_detail_id, **kwargs):
        order_detail = cls.read(order_detail_id)
        if order_detail:
            for key, value in kwargs.items():
                setattr(order_detail, key, value)
            order_detail.save()
            return order_detail
        return None

    @classmethod
    def delete(cls, order_detail_id):
        order_detail = cls.read(order_detail_id)
        if order_detail:
            order_detail.delete()
            return True
        return False


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.code

    @classmethod
    def create(cls, code, discount, valid_from, valid_to, active=True):
        coupon = cls(code=code, discount=discount, valid_from=valid_from, valid_to=valid_to, active=active)
        coupon.save()
        return coupon

    @classmethod
    def read(cls, coupon_id):
        try:
            return cls.objects.get(id=coupon_id)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def update(cls, coupon_id, **kwargs):
        coupon = cls.read(coupon_id)
        if coupon:
            for key, value in kwargs.items():
                setattr(coupon, key, value)
            coupon.save()
            return coupon
        return None

    @classmethod
    def delete(cls, coupon_id):
        coupon = cls.read(coupon_id)
        if coupon:
            coupon.delete()
            return True
        return False


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def create(cls, first_name, last_name, email, phone_number=None, address=''):
        customer = cls(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, address=address)
        customer.save()
        return customer

    @classmethod
    def read(cls, customer_id):
        try:
            return cls.objects.get(id=customer_id)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def update(cls, customer_id, **kwargs):
        customer = cls.read(customer_id)
        if customer:
            for key, value in kwargs.items():
                setattr(customer, key, value)
            customer.save()
            return customer
        return None

    @classmethod
    def delete(cls, customer_id):
        customer = cls.read(customer_id)
        if customer:
            customer.delete()
            return True
        return False


class Refund(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='refunds')
    reason = models.TextField()
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Refund for Order {self.order.id}'

    @classmethod
    def create(cls, order, reason, accepted=False):
        refund = cls(order=order, reason=reason, accepted=accepted)
        refund.save()
        return refund

    @classmethod
    def read(cls, refund_id):
        try:
            return cls.objects.get(id=refund_id)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def update(cls, refund_id, **kwargs):
        refund = cls.read(refund_id)
        if refund:
            for key, value in kwargs.items():
                setattr(refund, key, value)
            refund.save()
            return refund
        return None

    @classmethod
    def delete(cls, refund_id):
        refund = cls.read(refund_id)
        if refund:
            refund.delete()
            return True
        return False


class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')
    rating = models.PositiveSmallIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Review by {self.customer.first_name} for {self.product.name}'

    @classmethod
    def create(cls, product, customer, rating, comment=None):
        review = cls(product=product, customer=customer, rating=rating, comment=comment)
        review.save()
        return review

    @classmethod
    def read(cls, review_id):
        try:
            return cls.objects.get(id=review_id)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def update(cls, review_id, **kwargs):
        review = cls.read(review_id)
        if review:
            for key, value in kwargs.items():
                setattr(review, key, value)
            review.save()
            return review
        return None

    @classmethod
    def delete(cls, review_id):
        review = cls.read(review_id)
        if review:
            review.delete()
            return True
        return False
