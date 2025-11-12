from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from .forms import ProductForm

from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Product, Order, Stock
from .forms import ClientForm, ProductForm, OrderForm, StockForm

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


# === CLIENTS ===
def clients_list(request):
    clients = Client.objects.all()
    return render(request, "clients.html", {"clients": clients})

def client_create(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("clients")
    else:
        form = ClientForm()
    return render(request, "form_template.html", {"form": form, "title": "Добавить клиента", "back": "clients"})

def client_update(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect("clients")
    else:
        form = ClientForm(instance=client)
    return render(request, "form_template.html", {"form": form, "title": "Редактировать клиента", "back": "clients"})

def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect("clients")
    return render(request, "confirm_delete.html", {"object": client, "back": "clients"})


# === ORDERS ===
def orders_list(request):
    orders = Order.objects.all()
    return render(request, "orders.html", {"orders": orders})

def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("orders")
    else:
        form = OrderForm()
    return render(request, "form_template.html", {"form": form, "title": "Создать заказ", "back": "orders"})

def order_update(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("orders")
    else:
        form = OrderForm(instance=order)
    return render(request, "form_template.html", {"form": form, "title": "Редактировать заказ", "back": "orders"})

def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
        order.delete()
        return redirect("orders")
    return render(request, "confirm_delete.html", {"object": order, "back": "orders"})


# === STOCKS ===
def stocks_list(request):
    stocks = Stock.objects.all()
    return render(request, "stocks.html", {"stocks": stocks})

def stock_create(request):
    if request.method == "POST":
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("stocks")
    else:
        form = StockForm()
    return render(request, "form_template.html", {"form": form, "title": "Добавить остаток", "back": "stocks"})

def stock_update(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect("stocks")
    else:
        form = StockForm(instance=stock)
    return render(request, "form_template.html", {"form": form, "title": "Редактировать остаток", "back": "stocks"})

def stock_delete(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        stock.delete()
        return redirect("stocks")
    return render(request, "confirm_delete.html", {"object": stock, "back": "stocks"})

