from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer,Product,Order,Tag

# Create your views here.
def home(request):
    customers=Customer.objects.all()
    orders=Order.objects.all()
    delever=Order.objects.filter(status='Delivered').count()
    total_orders=Order.objects.count()
    pending=Order.objects.filter(status='Pending').count()

    context={'customers':customers,'orders':orders,'total_orders':total_orders,'delever':delever,'pending':pending}
    return render(request,'account/dashboard.html',context)

def products(request):
    items=Product.objects.all()
    context={'items':items}

    return render(request,'account/product.html',context)

def customer(request,pk):
    customers=Customer.objects.get(id=pk)
    orders=customers.order_set.all()
    tot_orders=Order.objects.count()
    context={'cus':customers,'orders':orders,'tot':tot_orders}

    return render(request,'account/customer.html',context)