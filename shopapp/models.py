from django.db import models
# from django.contrib.auth.models import User

class Admin(models.Model):
    STATUS_CHOICES = (
        ('admin', 'Admin'),
        ('creater', 'Creater'),
    )
    # name = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, verbose_name='Ismi')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='admin', verbose_name='Status')
    def str(self):
        return self.name
    
class Category(models.Model):
    category_name = models.CharField(max_length=100,verbose_name='Maxsulot kategoriyasi')
    
    def str(self):
        return self.category_name

class Customer(models.Model):
    f_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Ism')
    l_name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Familiya')
    age = models.PositiveIntegerField(null=True, blank=True,verbose_name='Yoshi')
    # product = models.CharField(max_length=50, verbose_name='Maxsulotlar')
    
    def str(self):
        return f"{self.f_name} {self.l_name}"

class Items(models.Model):
    name = models.CharField(max_length=100)
    descriptions = models.TextField(verbose_name='Maxsulot haqida')
    price = models.DecimalField(max_digits=15, decimal_places=2)

    def str(self):
        return self.name
    
class Product(models.Model):

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Category')
    items_id = models.ForeignKey(Items, on_delete=models.CASCADE, verbose_name='Items')
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.TextField(max_length=100,null=False, blank=False,verbose_name='Maxsulot nomi')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Ishlab chiqarilgan vaqti')
    delete_day = models.IntegerField(verbose_name='Yaroqlilik muddati')
    price = models.IntegerField(null=False, blank=False, verbose_name='Narhi')

    def str(self):
        return self.name

class Shopcart(models.Model):
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Customer Id')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='Maxsulot narxi')
    total_price = models.DecimalField(max_digits=15, decimal_places=2,verbose_name='Karta hisobi')

    def str(self):
        return f"{self.customer_name} ning kartasi va unda {self.total_price} pul bor"
    

class PurchaseHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.customer.f_name} - {self.product.name} - {self.purchase_date}"