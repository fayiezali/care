from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User # إستيراد اسم المستخدم
from django.http import JsonResponse, HttpResponse
from django.http import HttpResponse, HttpResponseRedirect ,  HttpResponseBadRequest
from decimal import Decimal
from django.urls import reverse
from django.utils.timezone import now
from datetime import datetime
from django.contrib import messages

from .models import \
                    CustomerModel \
                    ,CategoryModel \
                    ,ProductModel \
                    ,OrderModel \
                    ,OrderDetailModel \
                    ,CouponModel \
                    ,RefundModel \
                    ,ReviewModel \
#___________________________________________
# (A) Create New Record #
#___________________________________________
# (A1)Create a Customer
def function_create_customer(request):
    #(001)
    if request.method == "POST":  # Retrieve POST data
        customerVariable_user   = request.POST.get('customerText_name')
        customerVariable_mobile = request.POST.get('customerText_mobile')

        #(002)
        # Fetch the CategoryModel instance  # Instance Must be a Name
        customerVariable_get_instance = get_object_or_404(
            User,
            username=customerVariable_user
        )
        #(003)
        # Create the ProductModel instance
        new_customerVariable = CustomerModel.objects.create(
            customerField_user=customerVariable_get_instance
            ,  # Ensure mobile is int
            customerField_mobile=int(customerVariable_mobile)
        )

        #(004)
        return HttpResponse(
        f'<h1> Successfully Done </h1>'
        # f'<h1> The Customer Profile is Created Automatically with The Creation Of a New User</h1>'
                            )

    #(005)
    return render(
    request,
    "categories/HttpResponse.html")
#=============================================
# (A2)Create a category
def function_create_category(request):
    #(001) Check if the request method is POST
    if request.method == "POST":
        categoryVariable_name= request.POST.get('categoryText_name')
        categoryVariable_slug= request.POST.get('categoryText_slug')
        categoryVariable_image= request.POST.get('productText_image')
        categoryVariable_available= request.POST.get('categoryText_availability')
        #(002)
        new_categoryVariable= CategoryModel.create(
            categoryField_name= categoryVariable_name
            , 
            categoryField_slug= categoryVariable_slug
            ,
            categoryField_image= categoryVariable_image # "Category_File_Photo/"
            ,
            categoryField_available= categoryVariable_available
                                                    )
            
        #(003)
        return HttpResponse(
        f'<h1> Successfully Done </h1>'
                            )
    #(004)
    return render(
    request,
    "categories/HttpResponse.html")
#=============================================
# (A3)Create a Product
def function_create_product(request):
    #(001)
    if request.method == "POST":  # Retrieve POST data
        productVariable_name = request.POST.get('productText_name')
        productVariable_category = request.POST.get('categoryText_name')
        productVariable_price = request.POST.get('productText_price')
        productVariable_stock = request.POST.get('productText_stock')
        productVariable_description = request.POST.get('productText_Description')
        productVariable_image = request.POST.get('productImage_image')
        productVariable_availability = request.POST.get('productBoolean_availability')
        #(002)
        # Fetch the CategoryModel instance  # Instance Must be a Name
        productVariable_get_instance = get_object_or_404(
            CategoryModel,
            categoryField_name=productVariable_category
        )
        #(003)
        # Create the ProductModel instance
        new_productVariable = ProductModel.objects.create(
            productField_name=productVariable_name
            ,
            productField_category=productVariable_get_instance
            ,  # Assign category instance
            productField_price=Decimal(productVariable_price)
            ,  # Ensure price is Decimal
            productField_stock=int(productVariable_stock)
            ,  # Ensure stock is int
            productField_description=productVariable_description,
            productField_image="Products_File_Photo/"
            ,  # Assuming productVariable_image should be processed
            productField_availability=productVariable_availability.lower() == 'true'  # Convert to boolean
        )
        #(004)
        return HttpResponse(
        f'<h1> Successfully Done </h1>'
                            )
    #(005)
    return render(
    request,
    "categories/HttpResponse.html")
#=============================================
# (A4)Create a Order
def function_create_order(request):
    #(001)
    if request.method == "POST": # Retrieve POST data
        orderVariable_customer = request.POST.get('orderText_customer')
        orderVariable_status = request.POST.get('orderText_status')
        orderVariable_date = request.POST.get('orderText_date')
        orderVariable_is_finished = request.POST.get('orderText_is_finished')

        # Fetch the CustomerModel instance  # Instance Must be a Name
        # This line fetches the CustomerModel 
        # instance whose associated User has the 
        # username specified in orderVariable_customer.
        # The __username lookup allows you to filter by
        # the username of the related User.
        #(002)
        customerVariable_get_instance = get_object_or_404(
            CustomerModel,customerField_user__username= orderVariable_customer)
        #(003)
        # Create the OrderModel instance
        new_orderVariable = OrderModel.objects.create(
            orderField_customer=customerVariable_get_instance
            ,
            orderField_status=orderVariable_status #"New"
            ,
            orderField_date=orderVariable_date      # "2042-05-06",
            ,
            orderField_is_finished=orderVariable_is_finished  # False
        )
        #(004)
        return HttpResponse('<h1> Successfully Done </h1>')
#=============================================
# (A5)Create a Order Detail
def function_create_orderDetail(request):
    if request.method == "POST":
        orderDetailVariable_order    = request.POST.get('OrderDetailText_order')
        orderDetailVariable_product  = request.POST.get('OrderDetailText_product')
        orderDetailVariable_quantity = request.POST.get('OrderDetailText_quantity')
        orderDetailVariable_price    = request.POST.get('OrderDetailText_price')

        # Validate input data
        if not orderDetailVariable_order or not orderDetailVariable_product or not orderDetailVariable_quantity or not orderDetailVariable_price:
            return HttpResponseBadRequest("All fields are required.")

        try:
            # Fetch the OrderModel instance  # Instance Must be a Name
            OrderVariable_get_instance = get_object_or_404(
                OrderModel,
                orderField_customer=orderDetailVariable_order
            )

            # Fetch the ProductModel instance  # Instance Must be a Name
            productVariable_get_instance = get_object_or_404(
                ProductModel,
                productField_name=orderDetailVariable_product
            )

            # Create the OrderDetailModel instance
            new_orderDetailVariable = OrderDetailModel.objects.create(
                OrderDetailField_order=OrderVariable_get_instance
                ,
                OrderDetailField_product=productVariable_get_instance
                ,
                OrderDetailField_quantity=int(orderDetailVariable_quantity)
                , 
                OrderDetailField_price=Decimal(orderDetailVariable_price)
                , 
            )

            return HttpResponse("Order detail created successfully.")

        except ValueError:
            return HttpResponseBadRequest("Invalid input for quantity or price.")
        except Exception as e:
            return HttpResponseBadRequest(f"An error occurred: {str(e)}")

#=============================================
# (A6)Create a Coupon
def function_create_coupon(request):
    #(001) Check if the request method is POST
    if request.method == "POST":
        CouponVariable_code      = request.POST.get('couponText_code')
        CouponVariable_discount  = request.POST.get('couponText_discount')
        CouponVariable_valid_from= request.POST.get('couponText_valid_from')
        CouponVariable_valid_to  = request.POST.get('couponText_valid_to')
        #(002)
        # Parse the date strings into datetime objects
        CouponVariable_valid_from = datetime.strptime(CouponVariable_valid_from, '%Y-%m-%d') # "2024-06-13",
        CouponVariable_valid_to = datetime.strptime(CouponVariable_valid_to, '%Y-%m-%d')
        #(003)
        new_couponVariable= CouponModel.create(
            CouponField_code= CouponVariable_code
            , 
            CouponField_discount= CouponVariable_discount
            ,
            CouponField_valid_from= CouponVariable_valid_from 
            ,
            CouponField_valid_to= CouponVariable_valid_to
                                                    )

        #(004)
        return HttpResponse(
        f'<h1> Successfully Done </h1>'
                            )
    #(005)
    return render(
    request,
    "categories/HttpResponse.html")
#=============================================
# (A7)Create a Refund
def function_create_refund(request):
    # (001) Check if the request method is POST
    if request.method == "POST":
        refundVariable_order = request.POST.get('refundText_order')
        refundVariable_reason = request.POST.get('refundText_reason')
        refundVariable_approved = request.POST.get('refundText_approved')
        
        # Check if all required fields are provided
        if not refundVariable_order or not refundVariable_reason or not refundVariable_approved:
            return HttpResponse('<h1>Missing data for creating refund</h1>', status=400)
        
        # (002) Fetch the OrderModel instance # Instance Must be a Name
        try:
            orderVariable_get_instance = get_object_or_404(OrderModel, orderField_customer=refundVariable_order)
        except OrderModel.DoesNotExist:
            return HttpResponse('<h1>Order not found</h1>', status=404)

        # (003) Create a new RefundModel instance
        new_refundVariable = RefundModel(
            refundField_order=orderVariable_get_instance,
            refundField_reason=refundVariable_reason,
            refundField_approved=refundVariable_approved
        )
        new_refundVariable.save()

        # (004) Return success response
        return HttpResponse(
        f'<h1> Successfully Done </h1>'
                            )
    # (005) Render the response for GET requests
    return render(request, "categories/HttpResponse.html")
#=============================================
# (A8)Create Review
def function_create_review(request):
    if request.method == "POST":
        ReviewVariable_product = request.POST.get('reviewText_product')
        ReviewVariable_customer = request.POST.get('reviewText_customer_id')
        ReviewVariable_rating = request.POST.get('reviewText_rating')
        ReviewVariable_comment = request.POST.get('reviewText_comment')

        # Validate input data
        if not ReviewVariable_product or not ReviewVariable_customer or not ReviewVariable_rating or not ReviewVariable_comment:
            return HttpResponseBadRequest("All fields are required.")

        try:
            # Fetch the ProductModel instance
            productVariable_get_instance = get_object_or_404(
                ProductModel,
                productField_name=ReviewVariable_product
            )
            # Fetch the CustomerModel instance  # Instance Must be a Name
            customerVariable_get_instance = get_object_or_404(
                CustomerModel,
                customerField_user=ReviewVariable_customer
            )

            # Ensure that rating is a valid integer or float
            try:
                ReviewVariable_rating = float(ReviewVariable_rating)
                if ReviewVariable_rating < 1 or ReviewVariable_rating > 5:
                    return HttpResponseBadRequest("Rating must be between 1 and 5.")
            except ValueError:
                return HttpResponseBadRequest("Rating must be a number.")

            # Create the ReviewModel instance
            new_reviewVariable = ReviewModel.objects.create(
                ReviewField_product=productVariable_get_instance,
                ReviewField_customer=customerVariable_get_instance,
                ReviewField_rating=ReviewVariable_rating,
                ReviewField_comment=ReviewVariable_comment
            )

            return HttpResponse('<h1> Successfully Done </h1>')

        except ProductModel.DoesNotExist:
            return HttpResponseBadRequest("Product not found.")
        except CustomerModel.DoesNotExist:
            return HttpResponseBadRequest("Customer not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"An error occurred: {e}")

    return render(request, "categories/HttpResponse.html")
#___________________________________________
# (B) Read/Detail Only One Record
#___________________________________________
# (B1) Read-Detail Customer
def function_read_detail_customer(request, customerParameter_pk):
    # customerParameter_pk=27
    customerVariable_read_detail_result = CustomerModel.read(customerParameter_pk)
    page_HTML_name="categories/HttpResponse.html"
    context={
        'customerVariable_read_detail_result': customerVariable_read_detail_result
            }
    return render(request , page_HTML_name , context
            )

# (B2) Read-Detail Category
def function_read_detail_category(request, categoryParameter_pk):
    categoryParameter_pk=7 # Default Value
    categoryVariable_read_detail_result = CategoryModel.read(categoryParameter_pk)
    page_HTML_name="categories/HttpResponse.html"
    context={
        'categoryVariable_read_detail_result': categoryVariable_read_detail_result
            }
    return render(request , page_HTML_name , context
            )

# (B3) Read-Detail Product
def function_read_detail_product(request, productParameter_pk):
    productParameter_pk=1 # Default Value
    productVariable_read_detail_result = ProductModel.read(productParameter_pk)
    page_HTML_name="categories/HttpResponse.html"
    context={
        'productVariable_read_detail_result': productVariable_read_detail_result
            }
    return render(request , page_HTML_name , context
            )

# (B4) Read-Detail Order
def function_read_detail_order(request, orderParameter_pk):
    orderParameter_pk=4 # Default Value
    orderVariable_read_detail_result = OrderModel.read(orderParameter_pk)
    page_HTML_name="categories/HttpResponse.html"
    context={
        'orderVariable_read_detail_result': orderVariable_read_detail_result
            }
    return render(request , page_HTML_name , context
            )

# (B5) Read-Detail OrderDetail
def function_read_detail_orderDetail(request, orderDetailParameter_pk):
    orderDetailParameter_pk=2 # Default Value
    orderDetailVariable_read_detail_result = OrderDetailModel.read(orderDetailParameter_pk)
    page_HTML_name="categories/HttpResponse.html"
    context={
        'orderDetailVariable_read_detail_result': orderDetailVariable_read_detail_result
            }
    return render(request , page_HTML_name , context
            )

# (B6) Read-Detail Coupon
def function_read_detail_coupon(request, couponParameter_pk):
    couponParameter_pk=2 # Default Value
    couponVariable_read_detail_result = CouponModel.read(couponParameter_pk)
    page_HTML_name="categories/HttpResponse.html"
    context={
        'couponVariable_read_detail_result': couponVariable_read_detail_result
            }
    return render(request , page_HTML_name , context
            )

# (B7) Read-Detail Refund
def function_read_detail_refund(request, refundParameter_pk):
    refundParameter_pk=2 # Default Value
    refundVariable_read_detail_result = RefundModel.read(refundParameter_pk)
    page_HTML_name="categories/HttpResponse.html"
    context={
        'refundVariable_read_detail_result': refundVariable_read_detail_result
            }
    return render(request , page_HTML_name , context
            )

# (B8) Read-Detail Review
def function_read_detail_review(request, reviewParameter_pk):
    reviewParameter_pk=1 # Default Value
    reviewVariable_read_detail_result = ReviewModel.read(reviewParameter_pk)
    page_HTML_name="categories/HttpResponse.html"
    context={
        'reviewVariable_read_detail_result': reviewVariable_read_detail_result
            }
    return render(request , page_HTML_name , context
            )
#___________________________________________
# (C) Update a Record
#___________________________________________
# (C1) Update customer
def function_update_customer(request, customerParameter_pk):
    updated_customer=None
    if request.method == 'POST':
        new_mobileVariable = request.POST.get('customerText_mobile')
        if new_mobileVariable:
            try:
                updated_customer = CustomerModel.update(
                pk=customerParameter_pk
                ,
                customerField_mobile=new_mobileVariable
                                                        )
                return JsonResponse(
                {
                "success": True, "message": "Updated Successfully."
                }
                                    )
            except CustomerModel.DoesNotExist:
                return JsonResponse(
                {
                "success": False, "message": "There were no results matching the search criteria - 01"
                }
                )
        else:
            return JsonResponse(
            {
            "success": False, "message": "There were no results matching the search criteria - 02"
            }
            )
    else:
        # page_HTML_name="categories/update_customer.html"
        page_HTML_name="categories/HttpResponse.html"
        context={
        'customerParameter_pk': customerParameter_pk 
        ,
        'updated_customer': updated_customer
            }
        return render(request , page_HTML_name , context
            )
#___________________________________________
# (C2) Update Category
def function_update_category(request, categoryParameter_pk):
    categoryVariable_update_result=None
    if request.method == 'POST':
        categoryVariable_name      = request.POST.get('categoryText_name')
        categoryVariable_slug      = request.POST.get('categoryText_slug')
        categoryVariable_image     = request.POST.get('categoryText_image')
        categoryVariable_available = request.POST.get('categoryText_available')
        # If All Not empty
        if all([
        categoryVariable_name
        , 
        categoryVariable_slug
        , 
        categoryVariable_image
        ,
        categoryVariable_available
                ]):
            try:
                categoryVariable_update_result = CategoryModel.update(
                pk=categoryParameter_pk
                ,
                categoryField_name=categoryVariable_name
                ,
                categoryField_slug=categoryVariable_slug

                ,
                categoryField_image=categoryVariable_image
                ,
                categoryField_available=categoryVariable_available
                                                                        )
                return JsonResponse({
                    "success": True,
                    "message": "Updated Successfully."
                })
            except CategoryModel.DoesNotExist:
                return JsonResponse({
                    "success": False,
                    "message": "No matching results found."
                })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid data submitted."
            })
    else:
        # page_HTML_name="categories/update_customer.html"
        page_HTML_name="categories/HttpResponse.html"
        context={
        'categoryParameter_pk': categoryParameter_pk 
        ,
        'categoryVariable_update_result': categoryVariable_update_result
            }
        return render(request , page_HTML_name , context
            )
#___________________________________________
# (C3) Update Product
def function_update_product(request, productParameter_pk):
    productVariable_update_result=None
    if request.method == 'POST':
        productVariable_name         = request.POST.get('productText_name')
        productVariable_category     = request.POST.get('productText_category')
        productVariable_price        = request.POST.get('productText_price')
        productVariable_stock        = request.POST.get('productText_stock')
        productVariable_description  = request.POST.get('productText_description')
        productVariable_image        = request.POST.get('productText_image')
        productVariable_availability = request.POST.get('productText_availability')
        #(002)
        # Fetch the CategoryModel instance # Instance Must be a Name
        categoryVariable_get_instance = get_object_or_404(
            CategoryModel,
            categoryField_name=productVariable_category
        )
        # If All Not empty
        if all([
        productVariable_name
        , 
        productVariable_category
        , 
        productVariable_price
        ,
        productVariable_stock
        , 
        productVariable_description
        , 
        productVariable_image
        ,
        productVariable_availability

                ]):
            try:
                productVariable_update_result = ProductModel.update(
                pk=productParameter_pk
                ,
                productField_name=productVariable_name
                ,
                productField_category=categoryVariable_get_instance
                ,
                productField_price=productVariable_price
                ,
                productField_stock=productVariable_stock
                ,
                productField_description=productVariable_description
                ,
                productField_image=productVariable_image
                ,
                productField_availability=productVariable_availability
                ,

                                                                        )
                return JsonResponse({
                    "success": True,
                    "message": "Updated Successfully."
                })
            except ProductModel.DoesNotExist:
                return JsonResponse({
                    "success": False,
                    "message": "No matching results found."
                })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid data submitted."
            })
    else:
        # page_HTML_name="categories/update_customer.html"
        page_HTML_name="categories/HttpResponse.html"
        context={
        'productParameter_pk': productParameter_pk 
        ,
        'productVariable_update_result': productVariable_update_result
            }
        return render(request , page_HTML_name , context
            )
#___________________________________________
# (C4) Update Order
def function_update_order(request, orderParameter_pk):
    orderVariable_update_result=None
    if request.method == 'POST':
        orderVariable_customer    = request.POST.get('orderText_customer')
        orderVariable_status      = request.POST.get('orderText_status')
        orderVariable_date        = request.POST.get('orderText_date')
        orderVariable_is_finished = request.POST.get('orderText_is_finished')
        #(002)
        # Fetch the CategoryModel instance # Instance Must be a Name
        #(002)
        # Fetch the CategoryModel instance  # Instance Must be a Name
        customerVariable_get_instance = get_object_or_404(
            CustomerModel,customerField_user__username=orderVariable_customer
        )
        # If All Not empty
        if all([
        orderVariable_customer
        , 
        orderVariable_status
        , 
        orderVariable_date
        , 
        orderVariable_is_finished
                ]):
            try:
                orderVariable_update_result = OrderModel.update(
                pk=orderParameter_pk
                ,
                orderField_customer=customerVariable_get_instance
                ,
                orderField_status=orderVariable_status
                ,
                orderField_date=orderVariable_date
                ,
                orderField_is_finished=orderVariable_is_finished
                                                                        )
                return JsonResponse({
                    "success": True,
                    "message": "Updated Successfully."
                })
            except OrderModel.DoesNotExist:
                return JsonResponse({
                    "success": False,
                    "message": "No matching results found."
                })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid data submitted."
            })
    else:
        # page_HTML_name="categories/update_customer.html"
        page_HTML_name="categories/HttpResponse.html"
        context={
        'orderParameter_pk': orderParameter_pk 
        ,
        'orderVariable_update_result': orderVariable_update_result
            }
        return render(request , page_HTML_name , context
            )
#___________________________________________
# (C5) Update OrderDetail
def function_update_orderDetail(request, orderDetailParameter_pk):
    orderDetailVariable_update_result = None
    if request.method == 'POST':
        orderDetailVariable_order    = request.POST.get('OrderDetailText_order')
        orderDetailVariable_product  = request.POST.get('OrderDetailText_product')
        orderDetailVariable_quantity = request.POST.get('OrderDetailText_quantity')
        orderDetailVariable_price    = request.POST.get('OrderDetailText_price')

        # Fetch the OrderModel instance
        orderVariable_get_instance = get_object_or_404(OrderModel, pk=orderDetailVariable_order)
        # Fetch the ProductModel instance
        productVariable_get_instance = get_object_or_404(ProductModel, pk=orderDetailVariable_product)

        # If All Not empty
        if all([
            orderDetailVariable_order,
            orderDetailVariable_product,
            orderDetailVariable_quantity,
            orderDetailVariable_price
        ]):
            try:
                orderDetailVariable_update_result = OrderDetailModel.update(
                    pk=orderDetailParameter_pk,
                    OrderDetailField_order=orderVariable_get_instance,
                    OrderDetailField_product=productVariable_get_instance,
                    OrderDetailField_quantity=int(orderDetailVariable_quantity),
                    OrderDetailField_price=Decimal(orderDetailVariable_price)
                )
                return JsonResponse({
                    "success": True,
                    "message": "Updated Successfully."
                })
            except OrderDetailModel.DoesNotExist:
                return JsonResponse({
                    "success": False,
                    "message": "No matching results found."
                })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid data submitted."
            })
    else:
        # page_HTML_name="categories/update_customer.html"
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'orderDetailParameter_pk': orderDetailParameter_pk,
            'orderDetailVariable_update_result': orderDetailVariable_update_result
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# (C6) Update Coupon
def function_update_coupon(request, couponParameter_pk):
    couponVariable_update_result = None
    if request.method == 'POST':
        couponVariable_code        = request.POST.get('CouponText_code')
        couponVariable_discount    = request.POST.get('CouponText_discount')
        couponVariable_valid_from  = request.POST.get('CouponText_valid_from')
        couponVariable_valid_to    = request.POST.get('CouponText_valid_to')

        #(002)
        # Parse the date strings into datetime objects
        couponVariable_valid_from = datetime.strptime(couponVariable_valid_from, '%Y-%m-%d') # "2024-06-13",
        couponVariable_valid_to = datetime.strptime(couponVariable_valid_to, '%Y-%m-%d')

        # If All Not empty
        if all([
            couponVariable_code,
            couponVariable_discount,
            couponVariable_valid_from,
            couponVariable_valid_to
        ]):
            try:
                couponVariable_update_result = CouponModel.update(
                    pk                    =couponParameter_pk,
                    CouponField_code      =couponVariable_code,
                    CouponField_discount  =couponVariable_discount,
                    CouponField_valid_from=couponVariable_valid_from,
                    CouponField_valid_to  =couponVariable_valid_to
                )
                return JsonResponse({
                    "success": True,
                    "message": "Updated Successfully."
                })
            except CouponModel.DoesNotExist:
                return JsonResponse({
                    "success": False,
                    "message": "No matching results found."
                })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid data submitted."
            })
    else:
        # page_HTML_name="categories/update_customer.html"
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'couponParameter_pk': couponParameter_pk,
            'couponVariable_update_result': couponVariable_update_result
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# (C7) Update Refund
def function_update_refund(request, refundParameter_pk):
    refundVariable_update_result=None
    if request.method == 'POST':
        refundVariable_order    = request.POST.get('refundText_order')
        refundVariable_reason   = request.POST.get('refundText_reason')
        refundVariable_approved = request.POST.get('refundText_approved')
        #(002)
        # Fetch the OrderModel instance
        refundVariable_get_instance = get_object_or_404(OrderModel, pk=refundVariable_order
        )
        # If All Not empty
        if all([
        refundVariable_order
        , 
        refundVariable_reason
        , 
        refundVariable_approved
                ]):
            try:
                refundVariable_update_result = RefundModel.update(
                pk=refundParameter_pk
                ,
                refundField_order=refundVariable_get_instance
                ,
                refundField_reason=refundVariable_reason
                ,
                refundField_approved=refundVariable_approved
                                                                        )
                return JsonResponse({
                    "success": True,
                    "message": "Updated Successfully."
                })
            except RefundModel.DoesNotExist:
                return JsonResponse({
                    "success": False,
                    "message": "No matching results found."
                })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid data submitted."
            })
    else:
        # page_HTML_name="categories/update_customer.html"
        page_HTML_name="categories/HttpResponse.html"
        context={
        'refundParameter_pk': refundParameter_pk 
        ,
        'refundVariable_update_result': refundVariable_update_result
            }
        return render(request , page_HTML_name , context
            )
#___________________________________________
# (C8) Update Review
def function_update_review(request, reviewParameter_pk):
    reviewVariable_update_result = None
    if request.method == 'POST':
        ReviewVariable_product = request.POST.get('ReviewText_product')
        ReviewVariable_customer= request.POST.get('ReviewText_customer')
        ReviewVariable_rating  = request.POST.get('ReviewText_rating')
        ReviewVariable_comment = request.POST.get('ReviewText_comment')

        # If All Not empty
        if all([
            ReviewVariable_product,
            ReviewVariable_customer,
            ReviewVariable_rating,
            ReviewVariable_comment
        ]):

            # Fetch the ProductModel instance
            productVariable_get_instance = get_object_or_404(ProductModel, pk=ReviewVariable_product)
            # Fetch the OrderModel instance
            customerVariable_get_instance = get_object_or_404(CustomerModel, pk=ReviewVariable_customer)
            print(productVariable_get_instance)
            print(customerVariable_get_instance)
            reviewVariable_update_result = ReviewModel.update(
                    pk=reviewParameter_pk,
                    ReviewField_product=productVariable_get_instance,
                    ReviewField_customer=customerVariable_get_instance,
                    ReviewField_rating=int(ReviewVariable_rating),
                    ReviewField_comment=ReviewVariable_comment
                )
            if reviewVariable_update_result:
                return JsonResponse({
                    "success": True,
                    "message": "Updated Successfully."
                })
            else:
                return JsonResponse({
                    "success": False,
                    "message": "Invalid data submitted."
                })
        else:
            return JsonResponse({
                "success": False,
                "message": "Invalid data submitted."
            })
    else:
            # page_HTML_name="categories/update_customer.html"
            page_HTML_name = "categories/HttpResponse.html"
            context = {
                'reviewParameter_pk': reviewParameter_pk,
                'reviewVariable_update_result': reviewVariable_update_result,
                'review': ReviewModel.read(reviewParameter_pk)
            }
            return render(request, page_HTML_name, context)
#___________________________________________
# (D) Delete a Record
#___________________________________________
# (D1) Delete a customer
def function_delete_customer_(request, pk):
    CustomerModel.objects.filter(pk=pk).delete()
    return JsonResponse({
        "success": True,
        "message": "Deleted Successfully."
    })

def function_delete_customer__(request):
    #(001)
    if request.method == "POST":  # Retrieve POST data
        customerVariable_id = request.POST.get('Text_id')
        if all([
            customerVariable_id,
            ]):
            CustomerModel.delete(customerVariable_id)
            return render(request, 'categories/Success.html',)
        else:
            return render(request, 'categories/Not_Success.html',)

    return render(request,"categories/HttpResponse.html")
# ------------OK------------------------------------
def function_return_HttpResponse(request):
    return render(request, 'categories/HttpResponse.html',)

def function_return_Success(request):
    return render(request, 'categories/Success.html',)

def function_return_Not_Success(request):
    return render(request, 'categories/Not_Success.html',)
#___________________________________________
# (D1) Delete  customer
def function_delete_customer(request):
    if request.method == 'POST':
        customerVariable_id = request.POST.get('Text_id')
        if all([customerVariable_id,
            ]):
            obj=CustomerModel.delete(customerVariable_id)
            return HttpResponseRedirect(reverse('url_Success'))  # Redirect after deletion
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after deletion
    else:
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'customerVariable_delete_result': obj
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# (D2) Delete  category
def function_delete_category(request):
    if request.method == 'POST':
        categoryVariable_id = request.POST.get('Text_id')
        if all([categoryVariable_id,
            ]):
            obj=CategoryModel.delete(categoryVariable_id)
            return HttpResponseRedirect(reverse('url_Success'))  # Redirect after deletion
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after deletion
    else:
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'customerVariable_delete_result': obj
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# # (D3) Delete  Product
def function_delete_product(request):
    if request.method == 'POST':
        productVariable_id = request.POST.get('Text_id')
        if all([productVariable_id,
            ]):
            obj=ProductModel.delete(productVariable_id)
            return HttpResponseRedirect(reverse('url_Success'))  # Redirect after deletion
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after deletion
    else:
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'customerVariable_delete_result': obj
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# # (D4) Delete  Order
def function_delete_order(request):
    if request.method == 'POST':
        orderVariable_id = request.POST.get('Text_id')
        if all([orderVariable_id,
            ]):
            obj=OrderModel.delete(orderVariable_id)
            return HttpResponseRedirect(reverse('url_Success'))  # Redirect after deletion
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after deletion
    else:
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'customerVariable_delete_result': obj
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# # (D5) Delete  OrderDetail
def function_delete_orderDetail(request):
    if request.method == 'POST':
        orderDetailVariable_id = request.POST.get('Text_id')
        if all([orderDetailVariable_id,
            ]):
            obj=OrderDetailModel.delete(orderDetailVariable_id)
            return HttpResponseRedirect(reverse('url_Success'))  # Redirect after deletion
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after deletion
    else:
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'customerVariable_delete_result': obj
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# # (D6) Delete  coupon
def function_delete_coupon(request):
    if request.method == 'POST':
        couponVariable_id = request.POST.get('Text_id')
        if all([couponVariable_id,
            ]):
            obj=CouponModel.delete(couponVariable_id)
            return HttpResponseRedirect(reverse('url_Success'))  # Redirect after deletion
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after deletion
    else:
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'customerVariable_delete_result': obj
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# # (D7) Delete  Refund
def function_delete_refund(request):
    if request.method == 'POST':
        refundVariable_id = request.POST.get('Text_id')
        if all([refundVariable_id,
            ]):
            obj=RefundModel.delete(refundVariable_id)
            return HttpResponseRedirect(reverse('url_Success'))  # Redirect after deletion
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after deletion
    else:
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'customerVariable_delete_result': obj
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# # (D8) Delete  Review
def function_delete_review(request):
    if request.method == 'POST':
        customerVariable_id = request.POST.get('Text_id')
        if all([customerVariable_id,
            ]):
            obj=ReviewModel.delete(customerVariable_id)
            return HttpResponseRedirect(reverse('url_Success'))  # Redirect after deletion
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after deletion
    else:
        page_HTML_name = "categories/HttpResponse.html"
        context = {
            'customerVariable_delete_result': obj
        }
        return render(request, page_HTML_name, context)
#___________________________________________
# (E) Get All Records / List All Records
#___________________________________________
# (E1) List all customers
def function_read_all_customer(request):
    customerVariable_read_all_result = CustomerModel.all()
    page_HTML_name="categories/HttpResponse.html"
    context={
        'customerVariable_read_all_result': customerVariable_read_all_result
            }
    return render(request , page_HTML_name , context
            )

# (E2) Read All Category
def function_read_all_category(request):
    categoryVariable_read_all_result = CategoryModel.all()
    page_HTML_name="categories/HttpResponse.html"
    context={
        'categoryVariable_read_all_result': categoryVariable_read_all_result
            }
    return render(request , page_HTML_name , context
            )

# (E3) Read All Product
def function_read_all_product(request):
    productVariable_read_all_result = ProductModel.all()
    page_HTML_name="categories/HttpResponse.html"
    context={
        'productVariable_read_all_result': productVariable_read_all_result
            }
    return render(request , page_HTML_name , context
            )

# (E4) Read All Order
def function_read_all_order(request):
    orderVariable_read_all_result = OrderModel.all()
    page_HTML_name="categories/HttpResponse.html"
    context={
        'orderVariable_read_all_result': orderVariable_read_all_result
            }
    return render(request , page_HTML_name , context
            )

# (E5) Read All OrderDetail
def function_read_all_orderDetail(request):
    orderDetailVariable_read_all_result = OrderDetailModel.all()
    page_HTML_name="categories/HttpResponse.html"
    context={
        'orderDetailVariable_read_all_result': orderDetailVariable_read_all_result
            }
    return render(request , page_HTML_name , context
            )

# (E6) Read All Coupon
def function_read_all_coupon(request):
    couponVariable_read_all_result = CouponModel.all()
    page_HTML_name="categories/HttpResponse.html"
    context={
        'couponVariable_read_all_result': couponVariable_read_all_result
            }
    return render(request , page_HTML_name , context
            )

# (E7) Read All Refund
def function_read_all_refund(request):
    refundVariable_read_all_result = RefundModel.all()
    page_HTML_name="categories/HttpResponse.html"
    context={
        'refundVariable_read_all_result': refundVariable_read_all_result
            }
    return render(request , page_HTML_name , context
            )

# (E8) Read All Review
def function_read_all_review(request):
    reviewVariable_read_all_result = ReviewModel.all()
    page_HTML_name="categories/HttpResponse.html"
    context={
        'reviewVariable_read_all_result': reviewVariable_read_all_result
            }
    return render(request , page_HTML_name , context
            )
#___________________________________________
# (F) Search Records
#___________________________________________
# Do a case insensitive search for all records (__icontains)
# (F1) Search Customer  
def function_search_customer(request):
    if request.method == 'POST':
        customerVariable_user_search   = request.POST.get('Text_search_user')
        customerVariable_mobile_search = request.POST.get('Text_search_mobile')

        if all([
                # customerVariable_search_user,
                # customerVariable_search_mobile,
            ]):
            customerVariable_search_result = CustomerModel.search(
            # __icontains: Case-insensitive containment test.
            # customerField_user: Filed From CustomerModel
            # username: Filed From User Model

            customerField_user__username__icontains=customerVariable_user_search
            , 
            customerField_mobile__icontains=customerVariable_mobile_search 
            )
            page_HTML_name="categories/HttpResponse.html"
            context={
                'customerVariable_search_result': customerVariable_search_result
                    }
            return render(request , page_HTML_name , context
                    )
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after Search
    else:
        page_HTML_name="categories/HttpResponse.html"
        context={
            'customerVariable_search_result': customerVariable_search_result
                }
        return render(request , page_HTML_name , context
                )
# (F2) Search Category  
def function_search_category(request):
    if request.method == 'POST':
        categoryVariable_name_search      = request.POST.get('categoryText_name_search')
        categoryVariable_available_search = request.POST.get('categoryText_available_search')

        if all([
                # categoryVariable_name_search,
                # categoryVariable_available_search,
            ]):
            categoryVariable_search_result = CategoryModel.search(
            categoryField_name__icontains=categoryVariable_name_search
            , 
            categoryField_available__icontains=categoryVariable_available_search 
            )
            page_HTML_name="categories/HttpResponse.html"
            context={
                'categoryVariable_search_result': categoryVariable_search_result
                    }
            return render(request , page_HTML_name , context
                    )
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after Search
    else:
        page_HTML_name="categories/HttpResponse.html"
        context={
            'categoryVariable_search_result': categoryVariable_search_result
                }
        return render(request , page_HTML_name , context
                )
# (F3) Search Product  
def function_search_product(request):
    if request.method == 'POST':
        productVariable_name_search      = request.POST.get('productText_name_search')
        productVariable_category_search  = request.POST.get('productText_category_search')
        productVariable_price_search     = request.POST.get('productText_price_search')
        productVariable_stock_search     = request.POST.get('productText_stock_search')
        productVariable_available_search = request.POST.get('productText_available_search')

        if all([
                # productVariable_name_search     ,   
                # productVariable_category_search , 
                # productVariable_price_search    ,   
                # productVariable_stock_search    , 
                # productVariable_available_search 
            ]):
            productVariable_search_result = ProductModel.search(
            productField_name__icontains=productVariable_name_search
            , 
            # __icontains: Case-insensitive containment test.
            # productField_category: Filed From ProductModel
            # categoryField_name: Filed From CategoryModel
            # 
            productField_category__categoryField_name__icontains=productVariable_category_search 
            , 
            productField_price__icontains=productVariable_price_search 
            , 
            productField_stock__icontains=productVariable_stock_search 
            , 
            productField_availability__icontains=productVariable_available_search 
            )
            page_HTML_name="categories/HttpResponse.html"
            context={
                'productVariable_search_result': productVariable_search_result
                    }
            return render(request , page_HTML_name , context
                    )
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after Search
    else:
        page_HTML_name="categories/HttpResponse.html"
        context={
            'productVariable_search_result': productVariable_search_result
                }
        return render(request , page_HTML_name , context
                )
# (F4) Search Order  
def function_search_order(request):
    if request.method == 'POST':
        orderVariable_customer_search    = request.POST.get('orderText_customer_search')
        orderVariable_status_search      = request.POST.get('orderText_status_search')
        # orderVariable_date_search        = request.POST.get('orderText_date_search')
        orderVariable_is_finished_search = request.POST.get('orderText_is_finished_search')

        if all([
                # orderVariable_customer_search ,
                # orderVariable_status_search ,
                # orderVariable_date_search   ,
                # orderVariable_is_finished_search ,
            ]):
            # orderVariable_format_date = datetime.strptime(orderVariable_date_search, '%Y-%m-%d') # "2024-06-13",
            OrderVariable_search_result = OrderModel.search(
            # __icontains: Case-insensitive containment test.
            # orderField_customer: Filed From OrderModel
            # customerField_user: Filed From CustomerModel
            # username : Filed From User Model
            orderField_customer__customerField_user__username__icontains=orderVariable_customer_search 
            , 
            orderField_status__icontains=orderVariable_status_search 
            , 
            # orderField_date__icontains=orderVariable_format_date 
            # , 
            orderField_is_finished__icontains=orderVariable_is_finished_search 
            )
            page_HTML_name="categories/HttpResponse.html"
            context={
                'OrderVariable_search_result': OrderVariable_search_result
                    }
            return render(request , page_HTML_name , context
                    )
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after Search
    else:
        page_HTML_name="categories/HttpResponse.html"
        context={
            'OrderVariable_search_result': OrderVariable_search_result
                }
        return render(request , page_HTML_name , context
                )
# (F5) Search OrderDetail  
def function_search_orderDetail(request):
    if request.method == 'POST':
        OrderDetailVariable_order_search     = request.POST.get('OrderDetailVariable_order_search')
        OrderDetailVariable_product_search   = request.POST.get('OrderDetailVariable_product_search')
        OrderDetailVariable_quantity_search  = request.POST.get('OrderDetailVariable_quantity_search')
        OrderDetailVariable_price_search     = request.POST.get('OrderDetailVariable_price_search')

        if all([
        # OrderDetailVariable_order_search    ,
        # OrderDetailVariable_product_search  ,
        # OrderDetailVariable_quantity_search ,
        # OrderDetailVariable_price_search    ,
            ]):
            OrderDetailVariable_search_result = OrderDetailModel.search(
            # __icontains: Case-insensitive containment test.
            # OrderDetailField_order:Field From OrderDetailModel
            # orderField_customer: Filed From OrderModel
            # customerField_user: Filed From CustomerModel
            # username : Filed From User Model
            # OrderDetailField_order__orderField_customer__customerField_user__username__icontains=OrderDetailVariable_order_search 
            OrderDetailField_order__orderField_customer__customerField_user__username__icontains=OrderDetailVariable_order_search 
            , 
            OrderDetailField_product__productField_name__icontains=OrderDetailVariable_product_search 
            , 
            OrderDetailField_quantity__icontains=OrderDetailVariable_quantity_search 
            , 
            OrderDetailField_price__icontains=OrderDetailVariable_price_search 
            )
            page_HTML_name="categories/HttpResponse.html"
            context={
                'OrderDetailVariable_search_result': OrderDetailVariable_search_result
                    }
            return render(request , page_HTML_name , context
                    )
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after Search
    else:
        page_HTML_name="categories/HttpResponse.html"
        context={
            'OrderDetailVariable_search_result': OrderDetailVariable_search_result
                }
        return render(request , page_HTML_name , context
                )
# (F6) Search Coupon  
def function_search_coupon(request):
    if request.method == 'POST':
        CouponVariable_code_search       = request.POST.get('CouponText_code_search')
        CouponVariable_discount_search   = request.POST.get('CouponText_discount_search')
        CouponVariable_valid_from_search = request.POST.get('CouponText_valid_from_search')
        CouponVariable_valid_to_search   = request.POST.get('CouponText_valid_to_search')

        if all([
        # OrderDetailVariable_order_search    ,
        # OrderDetailVariable_product_search  ,
        # OrderDetailVariable_quantity_search ,
        # OrderDetailVariable_price_search    ,
            ]):
            couponVariable_search_result = CouponModel.search(
            # __icontains: Case-insensitive containment test.
            # orderField_customer: Filed From OrderModel
            # customerField_user: Filed From CustomerModel
            # username : Filed From User Model
            # OrderDetailField_order__orderField_customer__customerField_user__username__icontains=OrderDetailVariable_order_search 
            CouponField_code__icontains=CouponVariable_code_search 
            , 
            CouponField_discount__icontains=CouponVariable_discount_search 
            , 
            CouponField_valid_from__icontains=CouponVariable_valid_from_search 
            , 
            CouponField_valid_to__icontains=CouponVariable_valid_to_search 
            )
            page_HTML_name="categories/HttpResponse.html"
            context={
                'couponVariable_search_result': couponVariable_search_result
                    }
            return render(request , page_HTML_name , context
                    )
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after Search
    else:
        page_HTML_name="categories/HttpResponse.html"
        context={
            'couponVariable_search_result': couponVariable_search_result
                }
        return render(request , page_HTML_name , context
                )
# (F7) Search Refund  
def function_search_refund(request):
    if request.method == 'POST':
        refundVariable_order_search    = request.POST.get('refundText_order_search')
        refundVariable_reason_search   = request.POST.get('refundText_reason_search')
        refundVariable_approved_search = request.POST.get('refundText_approved_search')

        if all([
        # refundVariable_order_search ,
        # refundVariable_reason_search ,
        # refundVariable_approved_search
            ]):
            refundVariable_search_result = RefundModel.search(
            # __icontains: Case-insensitive containment test.
            # OrderDetailField_order:Field From OrderDetailModel
            # orderField_customer: Filed From OrderModel
            # customerField_user: Filed From CustomerModel
            # username : Filed From User Model
            # OrderDetailField_order__orderField_customer__customerField_user__username__icontains=OrderDetailVariable_order_search 
            refundField_order__orderField_customer__customerField_user__username__icontains=refundVariable_order_search 
            , 
            refundField_reason__icontains=refundVariable_reason_search 
            , 
            refundField_approved__icontains=refundVariable_approved_search 
            , 
            )
            page_HTML_name="categories/HttpResponse.html"
            context={
                'refundVariable_search_result': refundVariable_search_result
                    }
            return render(request , page_HTML_name , context
                    )
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after Search
    else:
        page_HTML_name="categories/HttpResponse.html"
        context={
            'refundVariable_search_result': refundVariable_search_result
                }
        return render(request , page_HTML_name , context
                )
# (F8) Search Review
def function_search_review(request):
    if request.method == 'POST':
        ReviewVariable_product_search   = request.POST.get('ReviewText_product_search')
        ReviewVariable_customer_search  = request.POST.get('ReviewText_customer_search')
        ReviewVariable_rating_search    = request.POST.get('ReviewText_rating_search')
        ReviewVariable_comment_search   = request.POST.get('ReviewText_comment_search')

        if all([
        # ReviewVariable_product_search  , 
        # ReviewVariable_customer_search , 
        # ReviewVariable_rating_search  ,  
        # ReviewVariable_comment_search  
            ]):
            reviewVariable_search_result = ReviewModel.search(
            # __icontains: Case-insensitive containment test.
            # OrderDetailField_order:Field From OrderDetailModel
            # orderField_customer: Filed From OrderModel
            # customerField_user: Filed From CustomerModel
            # username : Filed From User Model
            # OrderDetailField_order__orderField_customer__customerField_user__username__icontains=OrderDetailVariable_order_search 
            ReviewField_product__productField_name__icontains=ReviewVariable_product_search 
            , 
            # ReviewField_comment__customerField_user__username__icontains=ReviewVariable_customer_search 
            ReviewField_customer__customerField_user__username__icontains=ReviewVariable_customer_search 

            , 
            ReviewField_rating__icontains=ReviewVariable_rating_search 
            , 
            ReviewField_comment__icontains=ReviewVariable_comment_search 
            )
            page_HTML_name="categories/HttpResponse.html"
            context={
                'reviewVariable_search_result': reviewVariable_search_result
                    }
            return render(request , page_HTML_name , context
                    )
        else:
            return HttpResponseRedirect(reverse('url_Not_Success'))  # Redirect after Search
    else:
        page_HTML_name="categories/HttpResponse.html"
        context={
            'reviewVariable_search_result': reviewVariable_search_result
                }
        return render(request , page_HTML_name , context
                )













# # Search for categories by name
# found_categories = CategoryModel.search(categoryField_name="Electronics")

# # Search for products by name
# found_products = ProductModel.search(productField_name="Laptop")

# # Search for orders by status
# found_orders = OrderModel.search(orderField_status="Delivered")

# # Search for order details by product
# found_order_details = OrderDetailModel.search(OrderDetailField_product=product_instance)

# # Search for coupons by code
# found_coupons = CouponModel.search(CouponField_code="DISCOUNT10")

# # Search for refunds by approval status
# found_refunds = RefundModel.search(refundField_approved=True)

# # Search for reviews by rating
# found_reviews = ReviewModel.search(ReviewField_rating=5)
# #___________________________________________

