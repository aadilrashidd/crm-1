from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm ,CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register_page(request):
    form = CreateUserForm()
    if request.method== 'POST':
        form= CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'account created for ' + user)
            return redirect('login' )



    context = {'form': form}

    return render (request, 'accounts/register.html' , context)

def loginPage(request):
    if request.method=='POST' :
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request ,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: 
            messages.info(request, 'username or password incorrect')   
            return render(request, 'accounts/login.html' ,context) 
    context = {}

    return render(request, 'accounts/login.html' ,context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_orders = orders.count()
    total_delivered = Order.objects.filter(status='delivered').count()
    total_pending = Order.objects.filter(status='pending').count()

    context = {'orders': orders,
               'customers': customers,
               'total_orders': total_orders,
               'total_delivered': total_delivered,
               'total_pending': total_pending
               }

    return render(request, 'accounts/dashboard.html', context)

@login_required(login_url='login')
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html', {'products': products})

@login_required(login_url='login')
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    context = {'customer': customer,
               'orders': orders

               }
    return render(request, 'accounts/customer.html', context)

@login_required(login_url='login')
def createOrder(request):
    form = OrderForm()
    context = {'form', form}
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('')

    context = {'order': order}
    return render(request, 'accounts/delete.html', context)

@login_required(login_url='login')
def createProduct(request):
    form = ProductForm()
    context = {'form', form}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/products')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)
@login_required(login_url='login')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/products')

    context = {'form': form}
    return render(request, 'accounts/product_form.html', context)

@login_required(login_url='login')
def createCustomer(request):
    form = CustomerForm()
    context = {'form', form}
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = OrderForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/products')

    context = {'product': product}
    return render(request, 'accounts/delete_product.html', context)
