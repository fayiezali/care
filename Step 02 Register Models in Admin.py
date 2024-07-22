from django.contrib import admin
from .models import Categories, Products, Order, OrderDetails, Coupon, Customer, Refund, Review

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available', 'created_at', 'updated_at')
    list_filter = ('category', 'available')
    search_fields = ('name', 'description')
    ordering = ('-created_at',)
    # list_display = ('name', 'category', 'price', 'stock', 'description')
    # search_fields = ('name', 'category__name')
    # list_filter = ('category',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'customer', 'complete', 'date_ordered', 'status', 'updated_at')
    list_filter = ('complete', 'status')
    search_fields = ('order_id',)
    ordering = ('-created_at',)
    # list_display = ('customer', 'order_date', 'status')
    # search_fields = ('customer__first_name', 'customer__last_name', 'status')
    # list_filter = ('status', 'order_date')


@admin.register(OrderDetails)
class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'date_added')
    search_fields = ('order__id', 'product__name')
    # list_display = ('order', 'product', 'quantity', 'price')
    # search_fields = ('order__id', 'product__name')

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount', 'valid_from', 'valid_to', 'active')
    list_filter = ('active',)
    search_fields = ('code',)
    # list_display = ('code', 'discount', 'valid_from', 'valid_to')
    # search_fields = ('code',)
    # list_filter = ('valid_from', 'valid_to')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'email', 'phone_number', 'address')
    search_fields = ('first_name', 'last_name', 'email')
    # list_display = ('first_name', 'last_name', 'email', 'phone')
    # search_fields = ('first_name', 'last_name', 'email')
    # list_filter = ('first_name', 'last_name')

@admin.register(Refund)
class RefundAdmin(admin.ModelAdmin):
    list_display = ('order', 'reason', 'date_requested', 'accepted')
    list_filter = ('accepted',)
    search_fields = ('order__order_id',)
    # list_display = ('order', 'reason', 'approved')
    # search_fields = ('order__id', 'reason')
    # list_filter = ('approved',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'rating', 'comment', 'created_at', 'updated_at')
    list_filter = ('rating',)
    search_fields = ('product__name', 'customer__user__username')


# Register your models here.
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Refund, RefundAdmin)
admin.site.register(Review, ReviewAdmin)
























































