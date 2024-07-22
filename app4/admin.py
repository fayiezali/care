from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import \
                    CategoryModel \
                    ,ProductModel \
                    ,OrderModel \
                    ,OrderDetailModel \
                    ,CouponModel\
                    ,CustomerModel \
                    ,RefundModel \
                    ,ReviewModel \
# Admin Views for  All Models
# ___________________________________________
#(01)CUSTOMER-MODEL:
# ___________________________________________
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = (
        'customerField_user'
        ,'customerField_mobile'
        )
    list_filter = (
        'customerField_user'
        ,'customerField_mobile'
        ,
        )
    search_fields = (
        'customerField_user'
        ,'customerField_mobile'
        ,
        )
    ordering = (
        'customerField_user'
        ,'-customerField_mobile'
        ,
        )
#______________________________________________________
#(02)CATEGORY-MODEL:
#______________________________________________________
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = (
        'categoryField_name'
        ,'categoryField_slug'
        ,'categoryField_image'
        ,'categoryField_available'
        ,
        )
    list_filter = (
        'categoryField_name'
        ,'categoryField_available'
        ,
        )
    search_fields = (
        'categoryField_name'
        ,'categoryField_available'
        ,
        )
    ordering = (
        '-categoryField_name'
        ,
        )
#______________________________________________________
#(03)PRODUCT-MODEL:
#______________________________________________________
class ProductModelAdmin(admin.ModelAdmin):
    list_display = (
        'productField_name'
        ,'productField_category'
        ,'productField_price'
        ,'productField_stock'
        ,'productField_description'
        ,'productField_image'
        ,'productField_availability'
        ,
        )
    list_filter = (
        'productField_name'
        ,'productField_category'
        ,'productField_price'
        ,'productField_stock'
        ,'productField_availability'
        ,
        )
    search_fields = (
        'productField_name'
        ,'productField_category'
        ,'productField_price'
        ,'productField_stock'
        ,'productField_availability'
        ,
        )
    ordering = (
        'productField_name'
        ,'productField_category'
        ,'productField_price'
        ,'productField_stock'
        ,'productField_availability'
        ,
        )
#______________________________________________________
#(04)ORDER-MODEL:
#______________________________________________________
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        'orderField_customer'
        ,'orderField_status'
        ,'orderField_date'
        ,'orderField_is_finished'
        ,
        )
    list_filter = (
        'orderField_customer'
        ,'orderField_status'
        ,'orderField_date'
        ,'orderField_is_finished'
        ,
        )
    search_fields = (
        'orderField_customer'
        ,'orderField_status'
        ,'orderField_date'
        ,'orderField_is_finished'
        ,
        )
    ordering = (
        'orderField_status'
        ,'-orderField_date'
        ,'orderField_is_finished'
        ,
        ) 
# ___________________________________________
#(05)ORDER_DETAIL-MODEL:
# ___________________________________________
class OrderDetailModelAdmin(admin.ModelAdmin):
    list_display = (
        'OrderDetailField_order'
        ,'OrderDetailField_product'
        ,'OrderDetailField_quantity'
        ,'OrderDetailField_price'
        ,
        )
    list_filter = (
        'OrderDetailField_order'
        ,'OrderDetailField_product'
        ,'OrderDetailField_quantity'
        ,'OrderDetailField_price'
        ,
        )
    search_fields = (
        'OrderDetailField_order'
        ,'OrderDetailField_product'
        'OrderDetailField_quantity'
        ,'OrderDetailField_price'
        ,
        )
    ordering = (
        '-OrderDetailField_order'
        ,'OrderDetailField_product'
        ,
        )
#______________________________________________________
#(06)COUPON-MODEL:
#______________________________________________________
class CouponModelAdmin(admin.ModelAdmin):
    list_display = (
        'CouponField_code'
        ,'CouponField_discount'
        ,'CouponField_valid_from'
        ,'CouponField_valid_to'
        ,
        )
    list_filter = (
        'CouponField_discount'
        ,'CouponField_valid_from'
        ,'CouponField_valid_to'
        ,
        )
    search_fields = (
        'CouponField_code'
        ,'CouponField_discount'
        ,'CouponField_valid_from'
        ,'CouponField_valid_to'
        ,
        )
    ordering = (
        '-CouponField_code'
        ,'CouponField_discount'
        ,'-CouponField_valid_from'
        ,'-CouponField_valid_to'
        ,
        )
#______________________________________________________
#(07)REFUND-MODEL:
#______________________________________________________
class RefundModelAdmin(admin.ModelAdmin):
    list_display = (
        'refundField_order'
        ,'refundField_reason'
        ,'refundField_approved'
        ,
        )
    list_filter = (
        'refundField_order'
        ,'refundField_reason'
        ,'refundField_approved'
        ,
        )
    search_fields = (
        '-refundField_order'
        ,'refundField_reason'
        ,'-refundField_approved'
        ,
        )
    ordering = (
        '-refundField_order'
        ,'refundField_reason'
        ,'-refundField_approved'
        ,
        )
#______________________________________________________
#______________________________________________________
#(08)REFUND-MODEL:
#______________________________________________________
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = (
        'ReviewField_product'
        ,'ReviewField_customer'
        ,'ReviewField_rating'
        ,'ReviewField_comment'
        ,
        )
    list_filter = (
        'ReviewField_product'
        ,'ReviewField_customer'
        ,'ReviewField_rating'
        ,'ReviewField_comment'
        ,
        )
    search_fields = (
        'ReviewField_product'
        ,'ReviewField_customer'
        ,'ReviewField_rating'
        ,
        )
    ordering = (
        'ReviewField_product'
        ,'ReviewField_customer'
        ,'ReviewField_rating'
        ,'ReviewField_comment'
        ,
        )
#______________________________________________________
# Register your models here.
admin.site.register(CustomerModel   , CustomerModelAdmin)
admin.site.register(CategoryModel   , CategoryModelAdmin)
admin.site.register(ProductModel    , ProductModelAdmin)
admin.site.register(OrderModel      , OrderModelAdmin)
admin.site.register(OrderDetailModel, OrderDetailModelAdmin)
admin.site.register(CouponModel     , CouponModelAdmin)
admin.site.register(RefundModel     , RefundModelAdmin)
admin.site.register(ReviewModel     , ReviewModelAdmin)























































