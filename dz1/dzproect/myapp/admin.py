from django.contrib import admin
from .models import Client1, Product1, Order1


@admin.action(description='Удалить номер телефона')
def delete_number(modeladmin, request, queryset):
    queryset.update(number_phone='')


@admin.register(Client1)
class Client1Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'mail', 'number_phone', 'adress', 'data_register')
    list_per_page = 10
    ordering = ['name', 'data_register']
    search_fields = ['name']
    search_help_text = 'Поиск по полю описания продукта (Name)'
    readonly_fields = ['data_register']
    actions = [delete_number]

@admin.action(description='Обнуление товара')
def update_count(modeladmin, request, queryset):
    queryset.update(count=0)

@admin.register(Product1)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'count', 'date')
    list_per_page = 10
    ordering = ['name', 'count']
    search_fields = ['name']
    actions = [update_count]
    search_help_text = 'Поиск по полю описания продукта (Name)'
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name']
            },
        ),
        (
            'Подробности',
            {'classes': ['collapse'],
             'description': 'Категория товара и его подробное описание',
             'fields': [ 'description'],
             },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'count'],
            }
        ),
        (
            'Остальное',
            {
                'classes': ['collapse'],
                'description': 'Изображение',
                'fields': ['image_product'],

            }
        ),

    ]

@admin.action(description='Изменение имени заказа')
def update_client_order(modeladmin, request, queryset):
    queryset.update(client_order='New_order')

@admin.action(description='Изменение стоимости заказа')
def update_ptice(modeladmin, request, queryset):
    queryset.filter(total_price__gt=125).update(total_price=120)

@admin.register(Order1)
class Order1Admin(admin.ModelAdmin):
    list_display = ['client_order',  'total_price', 'date']
    list_per_page = 10
    ordering = ['total_price', 'date']
    search_fields = ['client_order']
    search_help_text = 'Поиск по имени заказа (client_order)'
    actions = [update_client_order, update_ptice]
    fields = ('client_order', 'product','total_price', 'date')
# Register your models here.
