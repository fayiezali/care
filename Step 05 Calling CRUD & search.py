#___________________________________________
from .models import \
                    CategoryModel \
                    ,ProductModel \
                    ,OrderModel \
                    ,OrderDetailModel \
                    ,CouponModel\
                    ,CustomerModel \
                    ,RefundModel \
                    ,ReviewModel \



#___________________________________________
# (1) Create New Record #
#___________________________________________

# Creating a new customer
new_customer = CustomerModel.create(
    customerField_user=some_user_instance,  # assuming some_user_instance is a User object
    customerField_mobile="1234567890"
)

# Create a category
new_category = CategoryModel.create(
    categoryField_name="Electronics", 
    categoryField_slug="electronics",
    categoryField_image="path/to/image.jpg",
    categoryField_available=True
)

# Create a product
new_product = ProductModel.create(
    productField_name="Laptop",
    productField_category=new_category,
    productField_price=Decimal('999.99'),
    productField_stock=10,
    productField_description="A high-performance laptop.",
    productField_image="path/to/product_image.jpg",
    productField_availability=True
)

# Create an order
new_order = OrderModel.create(
    orderField_customer=new_customer,
    orderField_status="New",
    orderField_is_finished=False
)

# Create order detail
new_order_detail = OrderDetailModel.create(
    OrderDetailField_order=new_order,
    OrderDetailField_product=new_product,
    OrderDetailField_quantity=2,
    OrderDetailField_price=new_product.productField_price
)

# Create a coupon
new_coupon = CouponModel.create(
    CouponField_code="DISCOUNT10",
    CouponField_discount=Decimal('10.00'),
    CouponField_valid_from=now(),
    CouponField_valid_to=now() + timedelta(days=30)
)

# Create a refund
new_refund = RefundModel.create(
    refundField_order=new_order,
    refundField_reason="Product damaged",
    refundField_approved=False
)

# Create a review
new_review = ReviewModel.create(
    ReviewField_product=new_product,
    ReviewField_customer=new_customer,
    ReviewField_rating=5,
    ReviewField_comment="Great product!"
)
#___________________________________________



#___________________________________________
#(2) Read/Detail Only One Record
#___________________________________________
# Read a customer
customer = CustomerModel.read(pk=1)

# Read a category
category = CategoryModel.read(pk=1)

# Read a product
product = ProductModel.read(pk=1)

# Read an order
order = OrderModel.read(pk=1)

# Read an order detail
order_detail = OrderDetailModel.read(pk=1)

# Read a coupon
coupon = CouponModel.read(pk=1)

# Read a refund
refund = RefundModel.read(pk=1)

# Read a review
review = ReviewModel.read(pk=1)
#___________________________________________



#___________________________________________
# (3) Update a Record
#___________________________________________
# Updating a customer
updated_customer = CustomerModel.update(
    pk=1,
    customerField_mobile="0987654321"
)

# Updating a category
updated_category = CategoryModel.update(
    pk=1,
    categoryField_name="Updated Category Name"
)

# Updating a product
updated_product = ProductModel.update(
    pk=1,
    productField_price=Decimal("599.99"),
    productField_stock=30
)

# Updating an order
updated_order = OrderModel.update(
    pk=1,
    orderField_status="Delivered"
)

# Updating an order detail
updated_order_detail = OrderDetailModel.update(
    pk=1,
    OrderDetailField_quantity=3
)

# Updating a coupon
updated_coupon = CouponModel.update(
    pk=1,
    CouponField_discount=Decimal("15.00")
)

# Updating a refund
updated_refund = RefundModel.update(
    pk=1,
    refundField_approved=True
)

# Updating a review
updated_review = ReviewModel.update(
    pk=1,
    ReviewField_rating=4
)
#___________________________________________



#___________________________________________
# (4) Delete a Record
#___________________________________________
# Delete a customer
CustomerModel.delete(pk=1)

# Delete a category
CategoryModel.delete(pk=1)

# Delete a product
ProductModel.delete(pk=1)

# Delete an order
OrderModel.delete(pk=1)

# Delete an order detail
OrderDetailModel.delete(pk=1)

# Delete a coupon
CouponModel.delete(pk=1)

# Delete a refund
RefundModel.delete(pk=1)

# Delete a review
ReviewModel.delete(pk=1)
#___________________________________________



#___________________________________________
# (5) Get All Records / List All Records
#___________________________________________
# List all customers
all_customers = CustomerModel.all()

# List all categories
all_categories = CategoryModel.all()

# List all products
all_products = ProductModel.all()

# List all orders
all_orders = OrderModel.all()

# List all order details
all_order_details = OrderDetailModel.all()

# List all coupons
all_coupons = CouponModel.all()

# List all refunds
all_refunds = RefundModel.all()

# List all reviews
all_reviews = ReviewModel.all()
#___________________________________________



#___________________________________________
# (6) Search Records
#___________________________________________
# Search for customers by mobile number
found_customers = CustomerModel.search(customerField_mobile="1234567890")

# Search for categories by name
found_categories = CategoryModel.search(categoryField_name="Electronics")

# Search for products by name
found_products = ProductModel.search(productField_name="Laptop")

# Search for orders by status
found_orders = OrderModel.search(orderField_status="Delivered")

# Search for order details by product
found_order_details = OrderDetailModel.search(OrderDetailField_product=product_instance)

# Search for coupons by code
found_coupons = CouponModel.search(CouponField_code="DISCOUNT10")

# Search for refunds by approval status
found_refunds = RefundModel.search(refundField_approved=True)

# Search for reviews by rating
found_reviews = ReviewModel.search(ReviewField_rating=5)
#___________________________________________
