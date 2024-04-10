from django.core.validators import MinValueValidator
from django.db import models

class Client1(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    number_phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=100)
    data_register = models.DateField(auto_now_add=True)


    def name_client(self):
        return f'{self.name} - {self.number_phone}'

class Product1(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    count = models.IntegerField()
    date = models.DateField(auto_now_add=True)



    def products_list(self):
        return f'{self.name} - цена = {self.price} - кол-во = {self.count}'




class Order1(models.Model):
    client_order = models.ForeignKey(Client1, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def calculate_total_amount(self):
        total = sum(product.price *
                    product.count for product in self.product.all())
        self.total_amount = total
        self.save()

    def order_list(self):
        return f'{self.client_order.name} - {self.product.name} - {self.total_price}'

class OrderProducts(models.Model):
    order = models.ForeignKey(Order1, on_delete=models.CASCADE)
    product = models.ForeignKey(Product1, on_delete=models.PROTECT)
    product_count = models.IntegerField(default=1, validators=[MinValueValidator(1)])

    def __str__(self):
        return f'{self.order.primary_key}. {self.product.name} - {self.product_count}'

# Create your models here.
