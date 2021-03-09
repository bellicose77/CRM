from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import OrderForm
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
def Order_page(request):
    form=OrderForm()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)

    context={'form':form}
    return render(request,'account/order_form.html',context)

def order_update(request,pk):
    froms=Order.objects.get(id=pk)
    form=OrderForm(instance=froms)

    if request.method == 'POST':
        form = OrderForm(request.POST,)
        if form.is_valid():
            form.save()
            return redirect(home)
    context = {'form':form}
    return render(request, 'account/order_form.html', context)

def delete_order(request,pk):
    order=Order.objects.get(id=pk)
    if request.method=="POST":
        order.delete()
        return redirect(home)
    context={"items":order}
    return render(request,'account/delete.html',context)