

```python
# Create a new category
new_category = Categories.create(name='New Category', description='Description of New Category')

# Read a category by ID
category = Categories.read(category_id=1)

# Update a category
updated_category = Categories.update(category_id=1, name='Updated Category', description='Updated Description')

# Delete a category
deleted = Categories.delete(category_id=1)

# Search for categories with specific criteria
filtered_categories = Categories.search(name__icontains='keyword')



# Create a new product
new_product = Products.create(category=new_category, name='New Product', description='Description of New Product', price=10.99, stock=100)

# Read a product by ID
product = Products.read(product_id=1)

# Update a product
updated_product = Products.update(product_id=1, price=9.99, stock=50)

# Delete a product
deleted = Products.delete(product_id=1)

# Search for products with specific criteria
filtered_products = Products.search(name__icontains='keyword')

# Create a new order
new_order = Order.create(customer=customer_instance)

# Read an order by ID
order = Order.read(order_id=1)

# Update an order
updated_order = Order.update(order_id=1, status='completed')

# Delete an order
deleted = Order.delete(order_id=1)

# Search for orders with specific criteria
filtered_orders = Order.search(status='pending')

# Create a new order detail
new_order_detail = OrderDetails.create(order=new_order, product=new_product, quantity=2, price=19.98)

# Read an order detail by ID
order_detail = OrderDetails.read(order_detail_id=1)

# Update an order detail
updated_order_detail = OrderDetails.update(order_detail_id=1, quantity=3)

# Delete an order detail
deleted = OrderDetails.delete(order_detail_id=1)

# Search for order details with specific criteria
filtered_order_details = OrderDetails.search(quantity__gte=2)

# Create a new coupon
new_coupon = Coupon.create(code='NEWCOUPON', discount=5, valid_from=datetime.now(), valid_to=datetime.now() + timedelta(days=30))

# Read a coupon by ID
coupon = Coupon.read(coupon_id=1)

# Update a coupon
updated_coupon = Coupon.update(coupon_id=1, discount=10)

# Delete a coupon
deleted = Coupon.delete(coupon_id=1)

# Search for coupons with specific criteria
filtered_coupons = Coupon.search(active=True)

# Create a new customer
new_customer = Customer.create(first_name='John', last_name='Doe', email='john.doe@example.com', address='123 Main St')

# Read a customer by ID
customer = Customer.read(customer_id=1)

# Update a customer
updated_customer = Customer.update(customer_id=1, phone_number='123-456-7890')

# Delete a customer
deleted = Customer.delete(customer_id=1)

# Search for customers with specific criteria
filtered_customers = Customer.search(email__icontains='example')

# Create a new refund
new_refund = Refund.create(order=new_order, reason='Product arrived damaged')

# Read a refund by ID
refund = Refund.read(refund_id=1)

# Update a refund
updated_refund = Refund.update(refund_id=1, accepted=True)

# Delete a refund
deleted = Refund.delete(refund_id=1)

# Search for refunds with specific criteria
filtered_refunds = Refund.search(accepted=False)

# Create a new review
new_review = Review.create(product=new_product, customer=new_customer, rating=4, comment='Great product!')

# Read a review by ID
review = Review.read(review_id=1)

# Update a review
updated_review = Review.update(review_id=1, rating=5)

# Delete a review
deleted = Review.delete(review_id=1)

# Search for reviews with specific criteria
filtered_reviews = Review.search(rating__gte=4)
```