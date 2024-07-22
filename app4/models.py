from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.utils.timezone import now

class CustomerModel(models.Model):
    customerField_user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Full Name "
    )
    customerField_mobile = models.CharField(
        max_length=20,
        verbose_name="Mobile Number "
    )

    def __str__(self):
        return str(self.customerField_user)

    class Meta:
        ordering = (
            'customerField_user',
            'customerField_mobile',
        )
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)
        # return cls.objects.filter(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.filter(pk=pk)
        obj.delete()
        return None  # Indicate that the object has been deleted

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

# (2)________________________________________
class CategoryModel(models.Model):
    categoryField_name=models.CharField(
        max_length=150
        ,verbose_name="Category Name")
    categoryField_slug=models.SlugField(
        max_length=150 
        ,unique=True
        ,verbose_name="Category Slug")
    categoryField_image=models.ImageField(
        upload_to='Category_File_Photo/' 
        ,default='Default_Image.png'
        ,verbose_name="Image Preview"  )
    categoryField_available = models.BooleanField(
        default=True
        ,verbose_name="Available")
    def __str__(self):
        return self.categoryField_name

    class Meta:
        ordering            = ('categoryField_name',)
        verbose_name        = "Categorie"
        verbose_name_plural = "Categories" 
#_________________________________________
# All OPERATIONS - ( CRUD + Search + All )
#_________________________________________
    #1111111111111111111111111111111111111
    # Create New Record #
    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)
    #2222222222222222222222222222222222222
#   # Read\Detail Only One Record #
    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)
    #3333333333333333333333333333333333333
    # Update  Record #
    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj
    #4444444444444444444444444444444444444
    # Delete  Record #
    @classmethod
    def delete(cls, pk):
        # obj = cls.objects.get(pk=pk)
        obj = cls.objects.filter(pk=pk)
        obj.delete()
    #5555555555555555555555555555555555555
    # All  Records #
    @classmethod
    def all(cls):
        return cls.objects.all()
    #6666666666666666666666666666666666666
    # Search  Record #
    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)
# (3)________________________________________
class ProductModel(models.Model):
    productField_name=models.CharField(
        max_length=200)
    productField_category= models.ForeignKey(
        CategoryModel
        ,on_delete=models.CASCADE
        ,verbose_name='Category Name'
        )
    productField_price=models.DecimalField(
        max_digits=10
        ,decimal_places=2
        ,default=0
        )
    productField_stock=models.PositiveIntegerField(
        default=0)
    productField_description=models.TextField()
    productField_image=models.ImageField(
        upload_to='Products_File_Photo/'
        )
    productField_availability = models.BooleanField(
        default=False
        )

    def __str__(self):
        return self.productField_name

    class Meta:
            ordering            = ('productField_name',)
            verbose_name        = "Product"
            verbose_name_plural = "Products" 

    # Create New Record #
    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    # Read\Detail Only One Record #
    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    # Update  Record #
    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    # Delete  Record #
    @classmethod
    def delete(cls, pk):
        # obj = cls.objects.get(pk=pk)
        obj = cls.objects.filter(pk=pk)
        obj.delete()

    # All  Records #
    @classmethod
    def all(cls):
        return cls.objects.all()

    # Search  Record #
    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)
# (4)________________________________________
class OrderModel(models.Model):
    ORDER_STATUS_CHOICES = (
        ('New'       , 'New'),
        ('Pending'   , 'Pending'),
        ('Delivered' , 'Delivered'),
        ('Cancelled' , 'Cancelled'),
        )
    orderField_customer=models.ForeignKey(
        CustomerModel
        ,on_delete=models.CASCADE
        )
    orderField_status=models.CharField(
        max_length=20
        ,choices=ORDER_STATUS_CHOICES
        ,default='New'
        )
    orderField_date=models.DateTimeField(
        auto_now_add=True
        )
    orderField_is_finished=models.BooleanField(
        default=False
        )

    def __str__(self):
            return str(self.id)

        # return f"Order {self.id}"
        # return str(f"Customer Name: \
        # {self.orderField_customer}")\
        # +" - " +\
        # str(f"Order No: {self.id}")

    class Meta:
            ordering            = ('-orderField_date'
                                    ,'orderField_customer',)
            verbose_name        = "Order"
            verbose_name_plural = "Orders" 

    # Create New Record #
    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    # Read\Detail Only One Record #
    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    # Update  Record #
    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    # Delete  Record #
    @classmethod
    def delete(cls, pk):
        # obj = cls.objects.get(pk=pk)
        obj = cls.objects.filter(pk=pk)
        obj.delete()

    # All  Records #
    @classmethod
    def all(cls):
        return cls.objects.all()

    # Search  Record #
    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)
# (5)________________________________________
class OrderDetailModel(models.Model):
    OrderDetailField_order=models.ForeignKey(
        OrderModel
        ,on_delete=models.CASCADE)
    OrderDetailField_product=models.ForeignKey(
        ProductModel
        ,on_delete=models.CASCADE)
    OrderDetailField_quantity=models.PositiveIntegerField()
    OrderDetailField_price=models.DecimalField(
        max_digits=10
        ,decimal_places=2)

    def __str__(self):
        # return str(self.OrderDetailField_order)
        return str(self.id)

    class Meta:
            ordering=(
                '-OrderDetailField_order'
                ,
                )
            verbose_name= "Order Detail"
            verbose_name_plural= "Order Detail" 

    # Create New Record #
    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    # Read\Detail Only One Record #
    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    # Update  Record #
    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    # Delete  Record #
    @classmethod
    def delete(cls, pk):
        # obj = cls.objects.get(pk=pk)
        obj = cls.objects.filter(pk=pk)
        obj.delete()

    # All  Records #
    @classmethod
    def all(cls):
        return cls.objects.all()

    # Search  Record #
    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)
# (6)________________________________________
class CouponModel(models.Model):
    CouponField_code=models.CharField(
        max_length=50)
    CouponField_discount=models.DecimalField(
        max_digits=5
        ,decimal_places=2)
    CouponField_valid_from=models.DateTimeField()
    CouponField_valid_to=models.DateTimeField()

    def __str__(self):
        return str(self.CouponField_code)

    class Meta:
            ordering=(
                '-CouponField_code'
                ,
                )
            verbose_name= "Coupon"
            verbose_name_plural= "Coupon" 

    # Create New Record #
    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    # Read\Detail Only One Record #
    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    # Update  Record #
    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    # Delete  Record #
    @classmethod
    def delete(cls, pk):
        # obj = cls.objects.get(pk=pk)
        obj = cls.objects.filter(pk=pk)
        obj.delete()

    # All  Records #
    @classmethod
    def all(cls):
        return cls.objects.all()

    # Search  Record #
    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)
# (7)________________________________________
class RefundModel(models.Model):
    refundField_order = models.ForeignKey(
        OrderModel
        ,on_delete=models.CASCADE)
    refundField_reason = models.TextField()
    refundField_approved = models.BooleanField(
        default=False)

    def __str__(self):
        return str(self.refundField_order)

    class Meta:
            ordering=(
                '-refundField_order'
                ,
                )
            verbose_name= "Refund"
            verbose_name_plural= "Refund" 

    # Create New Record #
    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    # Read\Detail Only One Record #
    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    # Update  Record #
    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    # Delete  Record #
    @classmethod
    def delete(cls, pk):
        # obj = cls.objects.get(pk=pk)
        obj = cls.objects.filter(pk=pk)
        obj.delete()

    # All  Records #
    @classmethod
    def all(cls):
        return cls.objects.all()

    # Search  Record #
    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)
# (8)________________________________________
class ReviewModel(models.Model):
    ReviewField_product=models.ForeignKey(
        ProductModel
        ,on_delete=models.CASCADE)
    ReviewField_customer=models.ForeignKey(
        CustomerModel
        ,on_delete=models.CASCADE)
    ReviewField_rating=models.PositiveIntegerField()
    ReviewField_comment=models.TextField()

    def __str__(self):
        return str(self.ReviewField_product)

    class Meta:
            ordering=(
                '-ReviewField_rating'
                ,'ReviewField_product'
                ,'ReviewField_customer'
                ,
                )
            verbose_name= "Review"
            verbose_name_plural= "Review" 

    # Create New Record #
    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    # Read\Detail Only One Record #
    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    # Update  Record #
    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    # Delete  Record #
    @classmethod
    def delete(cls, pk):
        # obj = cls.objects.get(pk=pk)
        obj = cls.objects.filter(pk=pk)
        obj.delete()

    # All  Records #
    @classmethod
    def all(cls):
        return cls.objects.all()

    # Search  Record #
    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)
