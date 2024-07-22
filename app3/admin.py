from django.contrib import admin
from .models import  *  # import all models
from django.utils.html import format_html
from django.contrib import admin
# from .models import Categories, Products, Order, OrderDetails, Coupon, Customer, Refund, Review

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available', 'created_at', 'updated_at')
    list_filter = ('available', 'created_at', 'updated_at', 'category')
    search_fields = ('name', 'category__name')
    ordering = ('-created_at',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at', 'updated_at')
    search_fields = ('customer__first_name', 'customer__last_name', 'id')
    ordering = ('-created_at',)

@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'valid_from', 'valid_to', 'active')
    list_filter = ('active', 'valid_from', 'valid_to')
    search_fields = ('code',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number')

@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ('order', 'reason', 'accepted', 'created_at')
    list_filter = ('accepted', 'created_at')
    search_fields = ('order__id',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'rating', 'comment', 'created_at', 'updated_at')
    list_filter = ('rating', 'created_at', 'updated_at')
    search_fields = ('product__name', 'customer__first_name', 'customer__last_name')
