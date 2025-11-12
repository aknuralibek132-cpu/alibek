from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm


# Create your views here.
from django.shortcuts import render
from .models import Client, Product, Order, Stock

def index(request):
    return render(request, "index.html")

def clients_list(request):
    clients = Client.objects.all()
    return render(request, "clients.html", {"clients": clients})


def products_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def orders_list(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})


def stocks_list(request):
    stocks = Stock.objects.all()
    return render(request, "stocks.html", {"stocks": stocks})



def products_list(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def product_create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm()
    return render(request, "product_form.html", {"form": form, "title": "Добавить продукт"})

def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect("products")
    else:
        form = ProductForm(instance=product)
    return render(request, "product_form.html", {"form": form, "title": "Редактировать продукт"})

def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        product.delete()
        return redirect("products")
    return render(request, "product_confirm_delete.html", {"product": product})
