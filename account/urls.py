from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('product/',views.products,name='product'),
    path('customer/',views.customer,name='customer'),
]