from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create_client/', views.create_client, name='create_client'),
    path('create_product/', views.create_product, name='create_product'),
    path('create_order/', views.create_order, name='create_order'),
    path('order_client/<int:client_id>', views.order_client, name='order_client'),
    path('client_last_orders/<int:client_id>', views.client_last_orders, name='client_last_orders')
]
