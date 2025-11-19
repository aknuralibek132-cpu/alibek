from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.clients_list, name='clients'),
    path('products/', views.products_list, name='products'),
    path('orders/', views.orders_list, name='orders'),
    path('stocks/', views.stocks_list, name='stocks'),

    path('clients/', views.clients_list, name='clients'),
    path('clients/add/', views.client_create, name='client_add'),
    path('clients/<int:pk>/edit/', views.client_update, name='client_edit'),
    path('clients/<int:pk>/delete/', views.client_delete, name='client_delete'),

    path('products/', views.products_list, name='products'),
    path('products/add/', views.product_create, name='product_add'),
    path('products/<int:pk>/edit/', views.product_update, name='product_edit'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),


    path('orders/', views.orders_list, name='orders'),
    path('orders/add/', views.order_create, name='order_add'),
    path('orders/<int:pk>/edit/', views.order_update, name='order_edit'),
    path('orders/<int:pk>/delete/', views.order_delete, name='order_delete'),


    path('stocks/', views.stocks_list, name='stocks'),
    path('stocks/add/', views.stock_create, name='stock_add'),
    path('stocks/<int:pk>/edit/', views.stock_update, name='stock_edit'),
    path('stocks/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)