# from django.db import models
# from django.contrib.auth.models import User
# from django.shortcuts import reverse
# # # ____________________________________________________________________
# class Categories(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name
# # # ____________________________________________________________________
# class Products(models.Model):
#     category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='products')
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     available = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name
# # # ____________________________________________________________________
# class Order(models.Model):
#     customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='orders')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('canceled', 'Canceled')])

#     def __str__(self):
#         return f'Order {self.id}'
# # # ____________________________________________________________________
# class OrderDetails(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_details')
#     product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='order_details')
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f'Order {self.order.id} - Product {self.product.name}'
# # # ____________________________________________________________________
# class Coupon(models.Model):
#     code = models.CharField(max_length=50, unique=True)
#     discount = models.DecimalField(max_digits=5, decimal_places=2)
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     active = models.BooleanField(default=True)

#     def __str__(self):
#         return self.code
# # # ____________________________________________________________________
# class Customer(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     address = models.TextField()

#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
# # # ____________________________________________________________________
# class Refund(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='refunds')
#     reason = models.TextField()
#     accepted = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'Refund for Order {self.order.id}'
# # # ____________________________________________________________________
# class Review(models.Model):
#     product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='reviews')
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reviews')
#     rating = models.PositiveSmallIntegerField()
#     comment = models.TextField(blank=True, null=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f'Review by {self.customer.first_name} for {self.product.name}'
# # ____________________________________________________________________