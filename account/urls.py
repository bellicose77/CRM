from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('product/',views.products,name='product'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('orderpage/',views.Order_page,name='order'),
    path('orderpage/<str:pk>/',views.order_update,name='order_update'),
    path('orderdelete/<str:pk>/', views.delete_order, name='order_delete'),
]