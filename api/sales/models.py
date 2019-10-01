from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    birth_date = models.DateField(db_index=True, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {} - {} - {}" \
            .format(self.first_name, self.last_name,
                    self.birth_date, self.email, self.user)


class Client(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, null=False, unique=True)
    phone = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return "{} - {} - {} - {}" \
            .format(self.name, self.address, self.email, self.phone)


class Area(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        return "{} - {}"\
            .format(self.name, self.clients)


class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    cost = models.DecimalField(default=1, null=False, decimal_places=2, max_digits=6)
    price = models.DecimalField(default=1, null=False, decimal_places=2, max_digits=6)
    stock = models.IntegerField(default=1, null=False)
    reorder = models.IntegerField(default=1, null=False)
    commited = models.IntegerField(default=1, null=False)
    active = models.BooleanField(default=True, null=False)
    image = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {} - {} - {} - {} - {} - {} - {} - {}" \
            .format(self.name, self.cost, self.price,
                    self.stock, self.reorder, self.commited,
                    self.active, self.image)


class Order(models.Model):
    ordered_at = models.DateTimeField(null=False)
    sent_at = models.DateTimeField(null=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderDetail')

    def __str__(self):
        return "{} - {} = {}" \
            .format(self.ordered_at, self.sent_at, self.products)


class OrderDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    price = models.DecimalField(default=1, null=False, decimal_places=2, max_digits=6)
    discount = models.FloatField(default=0, null=False)
    quantity = models.FloatField(default=1, null=False)
