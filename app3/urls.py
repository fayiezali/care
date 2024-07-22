# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path(
        'URL_address__categories/'
        , views.function__read_category_all
        , name='url__read_category_all')
        ,
    path(
        'URL_address__categories/<int:parameter__category_id>/'
        , views.function__read_category_detail
        , name='url__read_category_detail')
        ,
    # category_detail=category_read and category_read=category_detail
    # path('categories/read/<int:category_id>/', views.category_read, name='category_read'),
    # path('categories/create/', views.category_create, name='category_create'),
    # path('categories/update/<int:category_id>/', views.category_update, name='category_update'),
    # path('categories/delete/<int:category_id>/', views.category_delete, name='category_delete'),
]
