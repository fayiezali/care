from django.urls import path
from . import views

urlpatterns = [
#___________________________________________
# (A) Create New Record URLs
#___________________________________________
# (A1) Create customer
path(
    'URL_address_create_customer/create/'
    ,views.function_create_customer  
    ,name="url_create_customer"
    )
    ,
# (A2) Create Category
path(
    'URL_address_create_category/create/'
    ,views.function_create_category  
    ,name="url_create_category"
    )
    ,

# (A3) Create product
path(
    'URL_address_create_product/create/'
    ,views.function_create_product  
    ,name="url_create_product"
    )
    ,

# (A4) Create Order
path(
    'URL_address_create_order/create/'
    ,views.function_create_order  
    ,name="url_create_order"
    )
    ,

# (A5) Create OrderDetail
path(
    'URL_address_create_orderDetail/create/'
    ,views.function_create_orderDetail  
    ,name="url_create_orderDetail"
    )
    ,

# (A6) Create Coupon
path(
    'URL_address_create_coupon/create/'
    ,views.function_create_coupon  
    ,name="url_create_coupon"
    )
    ,

# (A7) Create Refund
path(
    'URL_address_create_refund/create/'
    ,views.function_create_refund  
    ,name="url_create_refund"
    )
    ,

# (A8) Create Refund
path(
    'URL_address_create_review/create/'
    ,views.function_create_review  
    ,name="url_create_review"
    )
    ,
                ]
urlpatterns += [
#___________________________________________
# (A) Create New Record URLs
#___________________________________________
# (B1) Read customer
path(
    'URL_address_read_detail_customer/<int:customerParameter_pk>/'
    ,views.function_read_detail_customer  
    ,name="url_read_detail_customer"
    )
    ,
# (B2) Read-Detail Category
path(
    'URL_address_read_detail_category/<int:categoryParameter_pk>/'
    ,views.function_read_detail_category  
    ,name="url_read_detail_category"
    )
    ,
# (B3) Read-Detail Product
path(
    'URL_address_read_detail_product/<int:productParameter_pk>/'
    ,views.function_read_detail_product  
    ,name="url_read_detail_product"
    )
    ,
# (B4) Read-Detail Order
path(
    'URL_address_read_detail_order/<int:orderParameter_pk>/'
    ,views.function_read_detail_order  
    ,name="url_read_detail_order"
    )
    ,
# (B5) Read-Detail OrderDetail
path(
    'URL_address_read_detail_orderDetail/<int:orderDetailParameter_pk>/'
    ,views.function_read_detail_orderDetail  
    ,name="url_read_detail_orderDetail"
    )
    ,
# (B6) Read-Detail Coupon
path(
    'URL_address_read_detail_coupon/<int:couponParameter_pk>/'
    ,views.function_read_detail_coupon  
    ,name="url_read_detail_coupon"
    )
    ,
# (B7) Read-Detail Refund
path(
    'URL_address_read_detail_refund/<int:refundParameter_pk>/'
    ,views.function_read_detail_refund  
    ,name="url_read_detail_refund"
    )
    ,

# (B8) Read-Detail Review
path(
    'URL_address_read_detail_review/<int:reviewParameter_pk>/'
    ,views.function_read_detail_review
    ,name="url_read_detail_review"
    )
    ,
                ]
urlpatterns += [
#___________________________________________
# (C) Update Record URLs
#___________________________________________
# (C1) Update customer
path('URL_address_update_customer/<int:customerParameter_pk>/'
    , views.function_update_customer
    , name='url_update_customer'
    )
    ,
# (C2) Update Category
path('URL_address_update_category/<int:categoryParameter_pk>/'
    , views.function_update_category
    , name='url_update_category'
    )
    ,
# (C3) Update Product
path('URL_address_update_product/<int:productParameter_pk>/'
    , views.function_update_product
    , name='url_update_product'
    )
    ,
# (C4) Update Order
path('URL_address_update_order/<int:orderParameter_pk>/'
    , views.function_update_order
    , name='url_update_order'
    )
    ,
# (C5) Update OrderDetail
path('URL_address_update_orderDetail/<int:orderDetailParameter_pk>/'
    , views.function_update_orderDetail
    , name='url_update_orderDetail'
    )
    ,
# (C6) Update Coupon
path('URL_address_update_coupon/<int:couponParameter_pk>/'
    , views.function_update_coupon
    , name='url_update_coupon'
    )
    ,
# (C7) Update Refund
path('URL_address_update_refund/<int:refundParameter_pk>/'
    , views.function_update_refund
    , name='url_update_refund'
    )
    ,
# (C8) Update Review
path('URL_address_update_review/<int:reviewParameter_pk>/'
    , views.function_update_review
    , name='url_update_review'
    )
    ,

                ]

# (D) Return (HttpResponse - Success - Not_Success) URLs
#___________________________________________
urlpatterns += [
# (DD1) 
    path('URL_address_HttpResponse/',
    views.function_return_HttpResponse
    , name='url_HttpResponse'
    )
    ,
    path('URL_address_Success/',
    views.function_return_Success
    , name='url_Success'
    )
    ,
    path('URL_address_Not_Success/',
    views.function_return_Not_Success
    , name='url_Not_Success'
    )
    ,
]
#___________________________________________
# (D) Delete Record URLs
#___________________________________________
urlpatterns += [
# (D1) Delete Customer
path('URL_address_delete_customer/',
    views.function_delete_customer
    , name='url_delete_customer'
    )
    ,

# (D2) Delete Category
path('URL_address_delete_category/',
    views.function_delete_category
    , name='url_delete_category'
    )
    ,
# (D3) Delete Product
path('URL_address_delete_product/',
    views.function_delete_product
    , name='url_delete_product'
    )
    ,
# (D4) Delete Order
path('URL_address_delete_order/',
    views.function_delete_order
    , name='url_delete_order'
    )
    ,
# (D5) Delete OrderDetail
path('URL_address_delete_orderDetail/',
    views.function_delete_orderDetail
    , name='url_delete_orderDetail'
    )
    ,
# (D6) Delete Coupon
path('URL_address_delete_coupon/',
    views.function_delete_coupon
    , name='url_delete_coupon'
    )
    ,
# (D7) Delete Refund
path('URL_address_delete_refund/',
    views.function_delete_refund
    , name='url_delete_refund'
    )
    ,
# (D8) Delete Review
path('URL_address_delete_review/',
    views.function_delete_review
    , name='url_delete_review'
    )
    ,
]
#___________________________________________
# (E) Read All Record URLs
#___________________________________________
urlpatterns += [
# (E1) Read All Customer
path(
    'URL_address_read_all_customer/'
    ,views.function_read_all_customer
    ,name='url_read_all_customer'
    )
    ,
# (E2) Read All Category
path(
    'URL_address_read_all_category/'
    ,views.function_read_all_category
    ,name='url_read_all_category'
    )
    ,
# (E3) Read All Product
path(
    'URL_address_read_all_product/'
    ,views.function_read_all_product
    ,name='url_read_all_product'
    )
    ,
# (E4) Read All Order
path(
    'URL_address_read_all_order/'
    ,views.function_read_all_order
    ,name='url_read_all_order'
    )
    ,
# (E5) Read All OrderDetail
path(
    'URL_address_read_all_orderDetail/'
    ,views.function_read_all_orderDetail
    ,name='url_read_all_orderDetail'
    )
    ,
# (E6) Read All Coupon
path(
    'URL_address_read_all_coupon/'
    ,views.function_read_all_coupon
    ,name='url_read_all_coupon'
    )
    ,
# (E7) Read All Refund
path(
    'URL_address_read_all_refund/'
    ,views.function_read_all_refund
    ,name='url_read_all_refund'
    )
    ,
# (E8) Read All Review
path(
    'URL_address_read_all_review/'
    ,views.function_read_all_review
    ,name='url_read_all_review'
    )
    ,
]
#___________________________________________
# (E) Search Record URLs
#___________________________________________
urlpatterns += [
# (E1) Search Customer
path(
    'URL_address_search_customer/'
    , views.function_search_customer
    , name='url_search_customer'
    )
    ,
# (E2) Search Category
path(
    'URL_address_search_category/'
    , views.function_search_category
    , name='url_search_category'
    )
    ,


# (E3) Search Product
path(
    'URL_address_search_product/'
    , views.function_search_product
    , name='url_search_product'
    )
    ,
# (E4) Search Order
path(
    'URL_address_search_order/'
    , views.function_search_order
    , name='url_search_order'
    )
    ,
# (E5) Search OrderDetail
path(
    'URL_address_search_orderDetail/'
    , views.function_search_orderDetail
    , name='url_search_orderDetail'
    )
    ,
# (E6) Search Coupon
path(
    'URL_address_search_coupon/'
    , views.function_search_coupon
    , name='url_search_coupon'
    )
    ,
# (E7) Search Refund
path(
    'URL_address_search_refund/'
    , views.function_search_refund
    , name='url_search_refund'
    )
    ,
# (E8) Search Review
path(
    'URL_address_search_review/'
    , views.function_search_review
    , name='url_search_review'
    )
    ,

]
# #___________________________________________
# # (1) Categories URLs
# #___________________________________________

# path(
#     'http-response-form'
#     , views.function_create_category  
#     , name="httpresponse"
#     )
#     ,
    
#     # path(
#     #     ''
#     #     , views.function_read_all_category
#     #     , name='categoryURLs_read_all'
#     #     )
#     #     ,
#     path('category_URL_address_detail/<int:categoryParameter_pk>/'
#         , views.function_read_detail_category
#         , name='categoryURLs_read_detail'
#         )
#         ,
#     path(
#         'category_URL_address_create/create/'
#         , views.function_create_category
#         , name='categoryURLs_create'
#         )
#         ,
#     # path(
#     #     'category_URL_address_update/<int:categoryParameter_pk>/update/'
#     #     , views.function_update_category
#     #     , name='categoryURLs_update'
#     #     )
#     #     ,
#     # path(
#     #     'category_URL_address_delete/<int:categoryParameter_pk>/delete/'
#     #     , views.function_delete_category
#     #     , name='categoryURLs_delete'
#     #     )
#     #     ,
#     # path(
#     #     'category_URL_address_search/search/'
#     #     , views.function_search_category
#     #     , name='categoryURLs_search'
#     #     )
#     #     ,
#___________________________________________
# (2) Products URLs
#___________________________________________
#         path(
#         'product_URL_address/'
#         , views.product_function_read_all
#         , name='product_url_read_all'
#         ),
#     path(
#         'product_URL_address/<int:pk>/'
#         , views.product_function_read_detail
#         , name='product_url_read_detail'
#         ),
#     path(
#         'product_URL_address/create/'
#         , views.product_function_create
#         , name='product_url_create'
#         ),
#     path(
#         'product_URL_address/<int:pk>/update/'
#         , views.product_function_update
#         , name='product_url_update'
#         ),
#     path(
#         'product_URL_address/<int:pk>/delete/'
#         , views.product_function_delete
#         , name='product_url_delete'
#         ),
#     path(
#         'product_URL_address/search/'
#         , views.product_function_search
#         , name='product_url_search'
#         ),
# #___________________________________________
# # (3) Orders URLs
# #___________________________________________
#     path(
#         'order_URL_address/'
#         , views.order_function_read_all
#         , name='order_url_read_all'
#         ),
#     path(
#         'order_URL_address/<int:pk>/'
#         , views.order_function_read_detail
#         , name='order_url_read_detail'
#         ),
#     path(
#         'order_URL_address/create/'
#         , views.order_function_create
#         , name='order_url_create'
#         ),
#     path(
#         'order_URL_address/<int:pk>/update/'
#         , views.order_function_update
#         , name='order_url_update'
#         ),
#     path(
#         'order_URL_address/<int:pk>/delete/'
#         , views.order_function_delete
#         , name='order_url_delete'
#         ),
#     path(
#         'order_URL_address/search/'
#         , views.order_function_search
#         , name='order_url_search'
#         ),
# #___________________________________________
# # (4) OrderDetails URLs
# #___________________________________________
#     path(
#         'orderdetail_URL_address/'
#         , views.orderdetail_function_read_all
#         , name='orderdetail_url_read_all'
#         ),
#     path(
#         'orderdetail_URL_address/<int:pk>/'
#         , views.orderdetail_function_read_detail
#         , name='orderdetail_url_read_detail'
#         ),
#     path(
#         'orderdetail_URL_address/create/'
#         , views.orderdetail_function_create
#         , name='orderdetail_url_create'
#         ),
#     path(
#         'orderdetail_URL_address/<int:pk>/update/'
#         , views.orderdetail_function_update
#         , name='orderdetail_url_update'
#         ),
#     path(
#         'orderdetail_URL_address/<int:pk>/delete/'
#         , views.orderdetail_function_delete
#         , name='orderdetail_url_delete'
#         ),
#     path('orderdetail_URL_address/search/'
#         , views.orderdetail_function_search
#         , name='orderdetail_url_search'
#         ),
# #___________________________________________
# # (5) Coupons URLs
# #___________________________________________
#     path(
#         'coupon_URL_address/'
#         , views.coupon_function_read_all
#         , name='coupon_url_read_all'
#         ),
#     path(
#         'coupon_URL_address/<int:pk>/'
#         , views.coupon_function_read_detail
#         , name='coupon_url_read_detail'
#         ),
#     path(
#         'coupon_URL_address/create/'
#         , views.coupon_function_create
#         , name='coupon_url_create'
#         ),
#     path(
#         'coupon_URL_address/<int:pk>/update/'
#         , views.coupon_function_update
#         , name='coupon_url_update'
#         ),
#     path(
#         'coupon_URL_address/<int:pk>/delete/'
#         , views.coupon_function_delete
#         , name='coupon_url_delete'
#         ),
#     path(
#         'coupon_URL_address/search/'
#         , views.coupon_function_search
#         , name='coupon_url_search'
#         ),
# #___________________________________________
# # (6) Customers URLs
# #___________________________________________
#     path(
#         'customer_URL_address/'
#         , views.customer_function_read_all
#         , name='customer_url_read_all'
#         ),
#     path(
#         'customer_URL_address/<int:pk>/'
#         , views.customer_function_read_detail
#         , name='customer_url_read_detail'
#         ),
#     path(
#         'customer_URL_address/create/'
#         , views.customer_function_create
#         , name='customer_url_create'
#         ),
#     path(
#         'customer_URL_address/<int:pk>/update/'
#         , views.customer_function_update
#         , name='customer_url_update'
#         ),
#     path(
#         'customer_URL_address/<int:pk>/delete/'
#         , views.customer_function_delete
#         , name='customer_url_delete'
#         ),
#     path(
#         'customer_URL_address/search/'
#         , views.customer_function_search
#         , name='customer_url_search'
#         ),
# #___________________________________________
# # (7) Refunds URLs
# #___________________________________________
#     path(
#         'refund_URL_address/'
#         , views.refund_function_read_all
#         , name='refund_url_read_all'
#         ),
#     path(
#         'refund_URL_address/<int:pk>/'
#         , views.refund_function_read_detail
#         , name='refund_url_read_detail'
#         ),
#     path(
#         'refund_URL_address/create/'
#         , views.refund_function_create
#         , name='refund_url_create'
#         ),
#     path(
#         'refund_URL_address/<int:pk>/update/'
#         , views.refund_function_update
#         , name='refund_url_update'
#         ),
#     path(
#         'refund_URL_address/<int:pk>/delete/'
#         , views.refund_function_delete
#         , name='refund_url_delete'
#         ),
#     path(
#         'refund_URL_address/search/'
#         , views.refund_function_search
#         , name='refund_url_search'
#         ),
# #___________________________________________
# # (8) Reviews URLs
# #___________________________________________
#     path(
#         'review_URL_address/'
#         , views.review_function_read_all
#         , name='review_url_read_all'
#         ),
#     path(
#         'review_URL_address/<int:pk>/'
#         , views.review_function_read_detail
#         , name='review_url_read_detail'
#         ),
#     path(
#         'review_URL_address/create/'
#         , views.review_function_create
#         , name='review_url_create'
#         ),
#     path(
#         'review_URL_address/<int:pk>/update/'
#         , views.review_function_update
#         , name='review_url_update'
#         ),
#     path(
#         'review_URL_address/<int:pk>/delete/'
#         , views.review_function_delete
#         , name='review_url_delete'
#         ),
#     path(
#         'review_URL_address/search/'
#         , views.review_function_search
#         , name='review_url_search'
#         ),

