
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class ModelCustomer(models.Model):
    customer_user   = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_mobile = models.CharField(max_length=20)
    # Add any additional fields related to the customer such as address, phone number, etc.
    
    def __str__(self):
        return str(self.customer_user)

    class Meta:
            ordering            = ('customer_user',)
            verbose_name        = "Customer"
            verbose_name_plural = "Customers" 
# ____________________________________________________________________________________________
class ModelCategory(models.Model):
    category_name = models.CharField(max_length=200)
    category_slug = models.SlugField(max_length=200 ,unique=True)

    def __str__(self):
        return self.category_name

    class Meta:
        ordering            = ('category_name',)
        verbose_name        = "Categorie"
        verbose_name_plural = "Categories" 
# ____________________________________________________________________________________________
class ModelProduct(models.Model):
    product_name         = models.CharField(max_length=200)
    product_category     = models.ForeignKey(ModelCategory, on_delete=models.CASCADE)
    product_price        = models.DecimalField(max_digits=10, decimal_places=2)
    product_stock        = models.PositiveIntegerField(default=0)
    product_description  = models.TextField()
    product_image        = models.ImageField(upload_to='products/')
    product_availability = models.BooleanField(default=False)
    def __str__(self):
        return self.product_name

    class Meta:
            ordering            = ('product_name',)
            verbose_name        = "Product"
            verbose_name_plural = "Producs" 
# ____________________________________________________________________________________________
class ModelOrder(models.Model):
    STATUS_CHOICES = (
        ('New'       , 'New'),
        ('Pending'   , 'Pending'),
        ('Delivered' , 'Delivered'),
        ('Cancelled' , 'Cancelled'),
    )
    order_customer    = models.ForeignKey(ModelCustomer, on_delete=models.CASCADE)
    order_status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    order_date        = models.DateTimeField(auto_now_add=True)
    order_is_finished = models.BooleanField(default=False)

    def __str__(self):
        # return str(self.id)
        # return f"Order {self.id}"
        return str(f"Customer Name: {self.order_customer}") +" - " + str(f"Order No: {self.id}")

    class Meta:
            ordering            = ('-order_date','order_customer',)
            verbose_name        = "Order"
            verbose_name_plural = "Orders" 
# ____________________________________________________________________________________________
class ModelCart(models.Model):
    # customer = models.ForeignKey(ModelCustomer, on_delete=models.CASCADE)
    cart_product       = models.ForeignKey(ModelProduct, on_delete=models.CASCADE, null=True)
    cart_order         = models.ForeignKey(ModelOrder   , on_delete = models.CASCADE)
    cart_quantity      = models.PositiveIntegerField(default=0)
    cart_details_price = models.PositiveIntegerField(default=0)
    cart_date_added    = models.DateTimeField(auto_now_add=True)

    def __str__(self): 
        return str(self.cart_product)
        # return f"{self.quantity} of {self.product.name} in Cart {self.cart.id}"
    class Meta:
            ordering            = ('-cart_product',)
            verbose_name        = "Cart"
            verbose_name_plural = "Carts" 
# ____________________________________________________________________________________________
 
 
# from django.core.validators import MinValueValidator, MaxValueValidator
# class Coupon(models.Model):
#     code = models.CharField(unique=True, max_length=50)
#     valid_from = models.DateTimeField()
#     valid_to = models.DateTimeField()
#     discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
#     active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = "Coupon"
#         verbose_name_plural = "Coupons"

#     def __str__(self):
#         return self.code


# class Coupon(models.Model):
#     coupon_code = models.CharField(max_length=30,unique=True)
#     valid_from = models.DateTimeField( null = True)
#     valid_to = models.DateTimeField( null = True )
#     discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
#     active = models.BooleanField(default=True)
#     def __str__(self):
#         return self.coupon_code
#     class  Meta:
#         ordering = ['-valid_to',]


# class Coupon(models.Model):
#     code = models.CharField(max_length=15)
#     amount = models.FloatField()

#     def __str__(self):
#         return self.code


# from django.core.validators import MinValueValidator, MaxValueValidator

# class Coupon(models.Model):
# 	code = models.CharField(max_length=25, unique=True)
# 	valid_from = models.DateTimeField()
# 	valid_to = models.DateTimeField()
# 	discount = models.IntegerField(
# 			validators=[MinValueValidator(0), MaxValueValidator(100)]
# 		)
# 	active = models.BooleanField(default=False)

# 	def __str__(self):
# 		return self.code



# class DiscountCoupon(models.Model):
#     coupon_code=models.CharField(max_length=10)
#     discount=models.DecimalField(max_digits=5,decimal_places=2)
#     active_from=models.DecimalField(max_digits=8,decimal_places=2)

#     def __str__(self):
#         return self.coupon_code



# class Discount(models.Model):
#     user=models.ForeignKey(Account,on_delete=models.CASCADE)
#     discount_appiled=models.DecimalField(max_digits=6,decimal_places=2)


#     def __str__(self):
#         return self.user.email


# class CheckoutDetail_MODEL(models.Model):
#     user = models.ForeignKey(User, on_delete=models.SET_NULL, db_constraint=False,null=True , blank=True)
#     order = models.ForeignKey(OrderMODEL, on_delete=models.SET_NULL, db_constraint=False,null=True , blank=True)
#     phone_number = models.CharField(max_length=10, blank=True, null=True)
#     total_amount = models.CharField(max_length=10, blank=True,null=True)
#     address = models.CharField(max_length=300, blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)
#     state = models.CharField(max_length=100, blank=True, null=True)
#     zipcode = models.CharField(max_length=100, blank=True, null=True)
#     payment = models.CharField(max_length=100, blank=True, null=True)
#     date_added_auto= models.DateTimeField(auto_now_add=True)     

#     # 'admin'display the field name on a page
#     # \: write code of more than 1 line in the Python interpreter
#     def __str__(self):
#         return  'phone_number: ' + str(self.phone_number) + '-' \
#                 'User Name: ' + str(self.user) + '-' \
#                 'Order Id: ' + str(self.order.id) 


# from django_countries.fields import CountryField
# class CheckoutAddress(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     street_address = models.CharField(max_length=100)
#     apartment_address = models.CharField(max_length=100)
#     country = CountryField(multiple=False)
#     zip = models.CharField(max_length=100)

#     def __str__(self):
#         return self.user.username
    
# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=100)
#     state = models.CharField(max_length=100)
#     zipcode = models.CharField(max_length=100)

#     def __str__(self):
#         return self.address


# class Address(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     street_address = models.CharField(max_length=100)
#     apartment_address = models.CharField(max_length=100)
#     country = CountryField(multiple=False)
#     zip = models.CharField(max_length=100)
#     address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
#     default = models.BooleanField(default=False)

#     def __str__(self):
#         return self.user.username

#     class Meta:
#         verbose_name_plural = 'Addresses'


# class Address(models.Model):
#     street=models.CharField(max_length=255)
#     city=models.CharField(max_length=255)
#     customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.street
    
 
#  class Orderss(models.Model):
#     payment_mode = [ 

#         ('COD','COD'),
#         ('PAYPAL','PAYPAL'),
#         ('RAZOR_PAY','RAZORPAY')
#     ]
#     payment_mode =  models.CharField(max_length=10, choices=payment_mode, default='COD')

#     user = models.ForeignKey(Account,on_delete=models.SET_NULL,null=True)
    
#     payment = models.ForeignKey(Payment,on_delete=models.SET_NULL, blank=True, null=True)

#     order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)


# class Tax_MODEL(models.Model):
#     """Django Model for State"""

#     tax_user               = models.OneToOneField( User, on_delete=models.SET_NULL, related_name='user_tax_relation',null=True, blank=True , verbose_name="User Tax")
#     tax_order              = models.OneToOneField( OrderMODEL, on_delete=models.SET_NULL, related_name='user_tax_relation',null=True, blank=True , verbose_name="Order Tax")
#     tax_rate               = models.DecimalField(max_digits=10,decimal_places=2 , default=15  , blank=True , null=True , verbose_name="Tax %")
#     divide_one_hundred     = models.DecimalField(max_digits=10,decimal_places=2 , default=100 , blank=True , null=True , verbose_name="100")
#     service_charges        = models.DecimalField(max_digits=10,decimal_places=2 , default=0   , blank=True , null=True , verbose_name="Service Charges")

#     # Create your models here.
#     class Meta:
#         ordering            = ('-tax_rate',)
#         verbose_name        = "Tax"
#         verbose_name_plural = "Taxs" 
#     #
#     # 'admin'display the field name on a page
#     def __str__(self):
#         return  'Tax Rate: ' + str(self.tax_rate) 
                

# class Refund(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     reason = models.TextField()
#     accepted = models.BooleanField(default=False)
#     email = models.EmailField()

#     def __str__(self):
#         return f"{self.pk}"

# class Review(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     content = models.TextField()
#     datetime = models.DateTimeField(default=now)
 
#     def __str__(self):
#         return str(self.customer) +  " Review: " + self.content



# class Reviews(models.Model):
#     product=models.ForeignKey(Product,on_delete=models.CASCADE)
#     user=models.ForeignKey(Account,on_delete= models.CASCADE)
#     description=models.TextField(max_length=300)
#     image=models.ImageField(upload_to='reviews',null=True,blank=True)  
#     created_date=models.DateTimeField(auto_now=True)
#     rating=models.IntegerField(null=True,blank=True)

#     def __str__(self):
#         return self.product.name

