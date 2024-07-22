
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

class ModelCustomer(models.Model):
    customer_user   = models.OneToOneField(User, 
                        on_delete=models.CASCADE)
    customer_mobile = models.CharField(max_length=20)
    #
    def __str__(self):
        return str(self.customer_user)
    #
    class Meta:
            ordering            = ('customer_user',)
            verbose_name        = "Customer"
            verbose_name_plural = "Customers" 
#(01)_______________________________________________________
class ModelCategory(models.Model):
    category_name      = models.CharField(max_length=200)
    category_slug      = models.SlugField(max_length=200 ,
                        unique=True)
    category_image     = models.ImageField(upload_to="Catgory_File_Photo/" , db_index=True  , blank=False , null=False , verbose_name="Image Preview"  ,default='Default_Image.png')
    category_availability = models.BooleanField(default=False                  , db_index=True  ,                            verbose_name="Available")

    #
    def __str__(self):
        return self.category_name
    #
    class Meta:
        ordering            = ('category_name',)
        verbose_name        = "Categorie"
        verbose_name_plural = "Categories" 
# ____________________________________________________________________________________________
class ModelProduct(models.Model):
    product_name         = models.CharField(max_length=200)
    product_slug         = models.SlugField(max_length=200 ,
                        unique=True)
    product_category     = models.ForeignKey(ModelCategory, 
                                on_delete=models.CASCADE)
    product_price        = models.DecimalField(max_digits=10,
                                decimal_places=2)
    product_stock        = models.PositiveIntegerField(default=0)
    product_description  = models.TextField()
    product_image        = models.ImageField(upload_to='products_File_Photo/')
    product_availability = models.BooleanField(default=False)
    #
    def __str__(self):
        return self.product_name
    #
    class Meta:
            ordering            = ('product_name',)
            verbose_name        = "Product"
            verbose_name_plural = "Producs" 
# ____________________________________________________________________________________________
class ModelOrder(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     products = models.ManyToManyField(Product, through='OrderProduct')
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = (
                    ('New'       , 'New'),
                    ('paid'      , 'Paid'),
                    ('shipped'   , 'Shipped'),
                    ('Pending'   , 'Pending'),
                    ('Delivered' , 'Delivered'),
                    ('Cancelled' , 'Cancelled'),
                    )
    order_customer       = models.ForeignKey(ModelCustomer, 
                        on_delete=models.SET_NULL, 
                        null=True, blank=True)
    # order_customer     = models.ForeignKey(ModelCustomer, 
    #                         on_delete=models.CASCADE)
    order_status         = models.CharField(max_length=20, 
                            choices=STATUS_CHOICES, default='New')
    order_date           = models.DateTimeField(auto_now_add=True)
    order_number         = models.CharField(max_length=200)
    order_total_amount   = models.PositiveIntegerField(default=0)
    order_is_finished    = models.BooleanField(default=False)
    #
    def __str__(self):
        # return str(self.id)
        # return f"Order {self.id}"
        # return f'{self.product.name} ({self.quantity})'
        # return f'{self.user.username}\'s Order {self.pk}'
        return str(f"Customer Name: {self.order_customer}") +" - " + str(f"Order No: {self.id}")
    
    # def __str__(self):
    #     return  'Customer Name : ' + str(self.order_customer) + ' - ' +\
    #             'Order No: ' + str(self.id)
    #
    class Meta:
            ordering            = ('-order_date','order_customer',)
            verbose_name        = "Order"
            verbose_name_plural = "Orders" 
# ____________________________________________________________________________________________
class ModelCart(models.Model):
    cart_product       = models.ForeignKey(ModelProduct, 
                                    on_delete=models.SET_NULL, null=True)
    cart_order         = models.ForeignKey(ModelOrder ,
                                    on_delete=models.SET_NULL, null=True)
    cart_quantity      = models.PositiveIntegerField(default=0)
    cart_price         = models.PositiveIntegerField(default=0)
    cart_creation_date = models.DateTimeField(auto_now_add=True)
    cart_image         = models.ImageField(upload_to='Cart_File_Photo/')
    #
    def __str__(self): 
        return str(self.cart_product)
	    # return f'{self.product.name} ({self.quantity})'
        # return f"{self.quantity} of {self.product.name} in Cart {self.cart.id}"
    class Meta:
            ordering            = ('-cart_product',)
            verbose_name        = "Cart"
            verbose_name_plural = "Carts" 
# ____________________________________________________________________________________________
class ModelCoupon(models.Model):
    coupon_code = models.CharField(unique=True, max_length=50)
    coupon_valid_from  = models.DateTimeField()
    coupon_valid_to    = models.DateTimeField()
    coupon_discount    = models.PositiveIntegerField(validators=[MinValueValidator(0),
                    MaxValueValidator(100)])
    coupon_discount    = models.DecimalField(max_digits=5,decimal_places=2)
    coupon_amount      = models.FloatField()
    coupon_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Coupon"
        verbose_name_plural = "Coupons"
        ordering = ['-coupon_valid_to',]

    def __str__(self):
        return self.coupon_code
        # return self.coupon_code
# ____________________________________________________________________________________________
class ModelRefund(models.Model):
    refund_order = models.ForeignKey(ModelOrder, on_delete=models.CASCADE)
    refund_reason = models.TextField()
    refund_processed = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Refund"
        verbose_name_plural = "Refunds"
        ordering = ['-refund_order',]

    def __str__(self):
        return f"Refund for Order {self.refund_order.id}"
# ____________________________________________________________________________________________
class ModelReviewsAndRating(models.Model):
    REVIEW_CHOICES = (
                    ('0'  , '0'),
                    ('1'  , '1'),
                    ('2'  , '2'),
                    ('3'  , '3'),
                    ('4'  , '4'),
                    ('5'  , '5'),
                    ('6'  , '6'),
                    ('7'  , '7'),
                    ('8'  , '8'),
                    ('9'  , '9'),
                    ('10' , '10'),
                    )

    review_product  = models.ForeignKey(ModelProduct, 
                        on_delete=models.CASCADE)
    review_customer = models.ForeignKey(ModelCustomer, 
                            on_delete=models.CASCADE)
    review_rating   = models.CharField(max_length=2, 
                            choices=REVIEW_CHOICES, default='1')
    review_comment = models.TextField()
    review_created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Reviews and Rating"
        verbose_name_plural = "Reviews and Rating"
        ordering = ['-review_product',]

    def __str__(self):
        return f"Review by {self.review_customer} for {self.review_product}"

