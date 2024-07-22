from django.contrib import admin
from .models import  *  # import all models
from django.utils.html import format_html
# from .models import Category, Product, Cart, Order, Coupon, Customer, Refund, Review

admin.site.register(ModelCustomer)
admin.site.register(ModelCategory)
admin.site.register(ModelProduct)
admin.site.register(ModelOrder)
admin.site.register(ModelCart)
admin.site.register(ModelCoupon)
admin.site.register(ModelRefund)
admin.site.register(ModelReviewsAndRating)