from django.urls import path
from . import views

urlpatterns = [
    # Categories URLs
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/<int:pk>/', views.categories_detail, name='categories_detail'),
    path('categories/create/', views.categories_create, name='categories_create'),
    path('categories/<int:pk>/update/', views.categories_update, name='categories_update'),
    path('categories/<int:pk>/delete/', views.categories_delete, name='categories_delete'),
    path('categories/search/', views.categories_search, name='categories_search'),

    # Products URLs
    path('products/', views.products_list, name='products_list'),
    path('products/<int:pk>/', views.products_detail, name='products_detail'),
    path('products/create/', views.products_create, name='products_create'),
    path('products/<int:pk>/update/', views.products_update, name='products_update'),
    path('products/<int:pk>/delete/', views.products_delete, name='products_delete'),
    path('products/search/', views.products_search, name='products_search'),

    # Orders URLs
    path('orders/', views.orders_list, name='orders_list'),
    path('orders/<int:pk>/', views.orders_detail, name='orders_detail'),
    path('orders/create/', views.orders_create, name='orders_create'),
    path('orders/<int:pk>/update/', views.orders_update, name='orders_update'),
    path('orders/<int:pk>/delete/', views.orders_delete, name='orders_delete'),
    path('orders/search/', views.orders_search, name='orders_search'),

    # OrderDetails URLs
    path('orderdetails/', views.orderdetails_list, name='orderdetails_list'),
    path('orderdetails/<int:pk>/', views.orderdetails_detail, name='orderdetails_detail'),
    path('orderdetails/create/', views.orderdetails_create, name='orderdetails_create'),
    path('orderdetails/<int:pk>/update/', views.orderdetails_update, name='orderdetails_update'),
    path('orderdetails/<int:pk>/delete/', views.orderdetails_delete, name='orderdetails_delete'),
    path('orderdetails/search/', views.orderdetails_search, name='orderdetails_search'),

    # Coupons URLs
    path('coupons/', views.coupons_list, name='coupons_list'),
    path('coupons/<int:pk>/', views.coupons_detail, name='coupons_detail'),
    path('coupons/create/', views.coupons_create, name='coupons_create'),
    path('coupons/<int:pk>/update/', views.coupons_update, name='coupons_update'),
    path('coupons/<int:pk>/delete/', views.coupons_delete, name='coupons_delete'),
    path('coupons/search/', views.coupons_search, name='coupons_search'),

    # Customers URLs
    path('customers/', views.customers_list, name='customers_list'),
    path('customers/<int:pk>/', views.customers_detail, name='customers_detail'),
    path('customers/create/', views.customers_create, name='customers_create'),
    path('customers/<int:pk>/update/', views.customers_update, name='customers_update'),
    path('customers/<int:pk>/delete/', views.customers_delete, name='customers_delete'),
    path('customers/search/', views.customers_search, name='customers_search'),

    # Refunds URLs
    path('refunds/', views.refunds_list, name='refunds_list'),
    path('refunds/<int:pk>/', views.refunds_detail, name='refunds_detail'),
    path('refunds/create/', views.refunds_create, name='refunds_create'),
    path('refunds/<int:pk>/update/', views.refunds_update, name='refunds_update'),
    path('refunds/<int:pk>/delete/', views.refunds_delete, name='refunds_delete'),
    path('refunds/search/', views.refunds_search, name='refunds_search'),

    # Reviews URLs
    path('reviews/', views.reviews_list, name='reviews_list'),
    path('reviews/<int:pk>/', views.reviews_detail, name='reviews_detail'),
    path('reviews/create/', views.reviews_create, name='reviews_create'),
    path('reviews/<int:pk>/update/', views.reviews_update, name='reviews_update'),
    path('reviews/<int:pk>/delete/', views.reviews_delete, name='reviews_delete'),
    path('reviews/search/', views.reviews_search, name='reviews_search'),
]
