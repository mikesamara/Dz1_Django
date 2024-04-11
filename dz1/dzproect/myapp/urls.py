from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create_client/', views.create_client, name='create_client'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_client/<int:client_id>', views.order_client, name='order_client'),
    path('product_image/', views.product_image, name='product_image'),
    path('all_product/', views.all_product, name='all_product'),
    path('client_last_orders/<int:client_id>', views.client_last_orders, name='client_last_orders'),
    path('create_products/<int:order_id>', views.create_products, name='create_products')
]
