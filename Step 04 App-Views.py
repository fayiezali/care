from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Categories, Products, Order, OrderDetails, Coupon, Customer, Refund, Review

# Categories Views
def categories_list(request):
    categories = Categories.all()
    return render(request, 'categories_list.html', {'categories': categories})

def categories_detail(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    return render(request, 'categories_detail.html', {'category': category})

def categories_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        Categories.create(name=name, description=description)
        return redirect('categories_list')
    return render(request, 'categories_form.html')

def categories_update(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    if request.method == 'POST':
        category.name = request.POST['name']
        category.description = request.POST['description']
        category.save()
        return redirect('categories_detail', pk=pk)
    return render(request, 'categories_form.html', {'category': category})

def categories_delete(request, pk):
    category = get_object_or_404(Categories, pk=pk)
    category.delete()
    return redirect('categories_list')

def categories_search(request):
    query = request.GET.get('query')
    categories = Categories.search(name__icontains=query)
    return render(request, 'categories_list.html', {'categories': categories})


# Products Views
def products_list(request):
    products = Products.all()
    return render(request, 'products_list.html', {'products': products})

def products_detail(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'products_detail.html', {'product': product})

def products_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        category = get_object_or_404(Categories, pk=request.POST['category'])
        price = request.POST['price']
        stock = request.POST['stock']
        description = request.POST['description']
        Products.create(name=name, category=category, price=price, stock=stock, description=description)
        return redirect('products_list')
    categories = Categories.all()
    return render(request, 'products_form.html', {'categories': categories})

def products_update(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        product.name = request.POST['name']
        product.category = get_object_or_404(Categories, pk=request.POST['category'])
        product.price = request.POST['price']
        product.stock = request.POST['stock']
        product.description = request.POST['description']
        product.save()
        return redirect('products_detail', pk=pk)
    categories = Categories.all()
    return render(request, 'products_form.html', {'product': product, 'categories': categories})

def products_delete(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect('products_list')

def products_search(request):
    query = request.GET.get('query')
    products = Products.search(name__icontains=query)
    return render(request, 'products_list.html', {'products': products})


# Orders Views
def orders_list(request):
    orders = Order.all()
    return render(request, 'orders_list.html', {'orders': orders})

def orders_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'orders_detail.html', {'order': order})

def orders_create(request):
    if request.method == 'POST':
        customer = get_object_or_404(Customer, pk=request.POST['customer'])
        status = request.POST['status']
        Order.create(customer=customer, status=status)
        return redirect('orders_list')
    customers = Customer.all()
    return render(request, 'orders_form.html', {'customers': customers})

def orders_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        order.customer = get_object_or_404(Customer, pk=request.POST['customer'])
        order.status = request.POST['status']
        order.save()
        return redirect('orders_detail', pk=pk)
    customers = Customer.all()
    return render(request, 'orders_form.html', {'order': order, 'customers': customers})

def orders_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('orders_list')

def orders_search(request):
    query = request.GET.get('query')
    orders = Order.search(status__icontains=query)
    return render(request, 'orders_list.html', {'orders': orders})


# OrderDetails Views
def orderdetails_list(request):
    orderdetails = OrderDetails.all()
    return render(request, 'orderdetails_list.html', {'orderdetails': orderdetails})

def orderdetails_detail(request, pk):
    orderdetail = get_object_or_404(OrderDetails, pk=pk)
    return render(request, 'orderdetails_detail.html', {'orderdetail': orderdetail})

def orderdetails_create(request):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=request.POST['order'])
        product = get_object_or_404(Products, pk=request.POST['product'])
        quantity = request.POST['quantity']
        price = request.POST['price']
        OrderDetails.create(order=order, product=product, quantity=quantity, price=price)
        return redirect('orderdetails_list')
    orders = Order.all()
    products = Products.all()
    return render(request, 'orderdetails_form.html', {'orders': orders, 'products': products})

def orderdetails_update(request, pk):
    orderdetail = get_object_or_404(OrderDetails, pk=pk)
    if request.method == 'POST':
        orderdetail.order = get_object_or_404(Order, pk=request.POST['order'])
        orderdetail.product = get_object_or_404(Products, pk=request.POST['product'])
        orderdetail.quantity = request.POST['quantity']
        orderdetail.price = request.POST['price']
        orderdetail.save()
        return redirect('orderdetails_detail', pk=pk)
    orders = Order.all()
    products = Products.all()
    return render(request, 'orderdetails_form.html', {'orderdetail': orderdetail, 'orders': orders, 'products': products})

def orderdetails_delete(request, pk):
    orderdetail = get_object_or_404(OrderDetails, pk=pk)
    orderdetail.delete()
    return redirect('orderdetails_list')

def orderdetails_search(request):
    query = request.GET.get('query')
    orderdetails = OrderDetails.search(order__id__icontains=query)
    return render(request, 'orderdetails_list.html', {'orderdetails': orderdetails})


# Coupons Views
def coupons_list(request):
    coupons = Coupon.all()
    return render(request, 'coupons_list.html', {'coupons': coupons})

def coupons_detail(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    return render(request, 'coupons_detail.html', {'coupon': coupon})

def coupons_create(request):
    if request.method == 'POST':
        code = request.POST['code']
        discount = request.POST['discount']
        valid_from = request.POST['valid_from']
        valid_to = request.POST['valid_to']
        Coupon.create(code=code, discount=discount, valid_from=valid_from, valid_to=valid_to)
        return redirect('coupons_list')
    return render(request, 'coupons_form.html')

def coupons_update(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    if request.method == 'POST':
        coupon.code = request.POST['code']
        coupon.discount = request.POST['discount']
        coupon.valid_from = request.POST['valid_from']
        coupon.valid_to = request.POST['valid_to']
        coupon.save()
        return redirect('coupons_detail', pk=pk)
    return render(request, 'coupons_form.html', {'coupon': coupon})

def coupons_delete(request, pk):
    coupon = get_object_or_404(Coupon, pk=pk)
    coupon.delete()
    return redirect('coupons_list')

def coupons_search(request):
    query = request.GET.get('query')
    coupons = Coupon.search(code__icontains=query)
    return render(request, 'coupons_list.html', {'coupons': coupons})


# Customers Views
def customers_list(request):
    customers = Customer.all()
    return render(request, 'customers_list.html', {'customers': customers})

def customers_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'customers_detail.html', {'customer': customer})

def customers_create(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        Customer.create(first_name=first_name, last_name=last_name, email=email, phone=phone)
        return redirect('customers_list')
    return render(request, 'customers_form.html')

def customers_update(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == 'POST':
        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.email = request.POST['email']
        customer.phone = request.POST['phone']
        customer.save()
        return redirect('customers_detail', pk=pk)
    return render(request, 'customers_form.html', {'customer': customer})

def customers_delete(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.delete()
    return redirect('customers_list')

def customers_search(request):
    query = request.GET.get('query')
    customers = Customer.search(first_name__icontains=query) | Customer.search(last_name__icontains=query)
    return render(request, 'customers_list.html', {'customers': customers})



# Refunds Views
def refunds_list(request):
    refunds = Refund.all()
    return render(request, 'refunds_list.html', {'refunds': refunds})

def refunds_detail(request, pk):
    refund = get_object_or_404(Refund, pk=pk)
    return render(request, 'refunds_detail.html', {'refund': refund})

def refunds_create(request):
    if request.method == 'POST':
        order = get_object_or_404(Order, pk=request.POST['order'])
        reason = request.POST['reason']
        approved = 'approved' in request.POST
        Refund.create(order=order, reason=reason, approved=approved)
        return redirect('refunds_list')
    orders = Order.all()
    return render(request, 'refunds_form.html', {'orders': orders})

def refunds_update(request, pk):
    refund = get_object_or_404(Refund, pk=pk)
    if request.method == 'POST':
        refund.order = get_object_or_404(Order, pk=request.POST['order'])
        refund.reason = request.POST['reason']
        refund.approved = 'approved' in request.POST
        refund.save()
        return redirect('refunds_detail', pk=pk)
    orders = Order.all()
    return render(request, 'refunds_form.html', {'refund': refund, 'orders': orders})

def refunds_delete(request, pk):
    refund = get_object_or_404(Refund, pk=pk)
    refund.delete()
    return redirect('refunds_list')

def refunds_search(request):
    query = request.GET.get('query')
    refunds = Refund.search(reason__icontains=query)
    return render(request, 'refunds_list.html', {'refunds': refunds})


# Reviews Views
def reviews_list(request):
    reviews = Review.all()
    return render(request, 'reviews_list.html', {'reviews': reviews})

def reviews_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'reviews_detail.html', {'review': review})

def reviews_create(request):
    if request.method == 'POST':
        product = get_object_or_404(Products, pk=request.POST['product'])
        customer = get_object_or_404(Customer, pk=request.POST['customer'])
        rating = request.POST['rating']
        comment = request.POST['comment']
        Review.create(product=product, customer=customer, rating=rating, comment=comment)
        return redirect('reviews_list')
    products = Products.all()
    customers = Customer.all()
    return render(request, 'reviews_form.html', {'products': products, 'customers': customers})

def reviews_update(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == 'POST':
        review.product = get_object_or_404(Products, pk=request.POST['product'])
        review.customer = get_object_or_404(Customer, pk=request.POST['customer'])
        review.rating = request.POST['rating']
        review.comment = request.POST['comment']
        review.save()
        return redirect('reviews_detail', pk=pk)
    products = Products.all()
    customers = Customer.all()
    return render(request, 'reviews_form.html', {'review': review, 'products': products, 'customers': customers})

def reviews_delete(request, pk):
    review = get_object_or_404(Review, pk=pk)
    review.delete()
    return redirect('reviews_list')

def reviews_search(request):
    query = request.GET.get('query')
    reviews = Review.search(comment__icontains=query)
    return render(request, 'reviews_list.html', {'reviews': reviews})


