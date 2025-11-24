from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=100, verbose_name='Sarlavha')
    content = models.TextField(blank=True, null=True, verbose_name='Text')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, null=True)
    bool = models.BooleanField(default=False, verbose_name='Bool')
    views = models.IntegerField(default=0)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='Category')

    def __str__(self):
        return self.title

    # class Meta:
    #     verbose_name = 'News'
    #     verbose_name_plural = 'News'
    #     ordering = ['-created']


class Supplier(models.Model):
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100, blank=True, null=True)
    contact_title = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    fax = models.CharField(max_length=50, blank=True, null=True)
    homepage = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class Product(models.Model):
    product_name = models.CharField(max_length=150)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity_per_unit = models.CharField(max_length=50, blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    units_in_stock = models.IntegerField(default=0)
    units_on_order = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=0)
    discontinued = models.BooleanField(default=False)

    def __str__(self):
        return self.product_name


class Customer(models.Model):
    company_name = models.CharField(max_length=100)
    # contact_name = models.CharField(max_length=100, blank=True, null=True)
    # contact_title = models.CharField(max_length=50, blank=True, null=True)
    # address = models.CharField(max_length=200, blank=True, null=True)
    # city = models.CharField(max_length=50, blank=True, null=True)
    # region = models.CharField(max_length=50, blank=True, null=True)
    # postal_code = models.CharField(max_length=20, blank=True, null=True)
    # country = models.CharField(max_length=50, blank=True, null=True)
    # phone = models.CharField(max_length=50, blank=True, null=True)
    # fax = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    # title = models.CharField(max_length=100, blank=True, null=True)
    # title_of_courtesy = models.CharField(max_length=50, blank=True, null=True)
    # birth_date = models.DateField(blank=True, null=True)
    # hire_date = models.DateField(blank=True, null=True)
    # address = models.CharField(max_length=200, blank=True, null=True)
    # city = models.CharField(max_length=50, blank=True, null=True)
    # region = models.CharField(max_length=50, blank=True, null=True)
    # postal_code = models.CharField(max_length=20, blank=True, null=True)
    # country = models.CharField(max_length=50, blank=True, null=True)
    # home_phone = models.CharField(max_length=50, blank=True, null=True)
    # extension = models.CharField(max_length=10, blank=True, null=True)
    # photo = models.BinaryField(blank=True, null=True)
    # notes = models.TextField(blank=True, null=True)
    # reports_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    # photo_path = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Region(models.Model):
    region_description = models.CharField(max_length=100)

    def __str__(self):
        return self.region_description


class Territory(models.Model):
    territory_description = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.territory_description


class EmployeeTerritory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    territory = models.ForeignKey(Territory, on_delete=models.CASCADE)


class Shipper(models.Model):
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.company_name


class Order(models.Model):
    # customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_date = models.DateField(blank=True, null=True)
    required_date = models.DateField(blank=True, null=True)
    shipped_date = models.DateField(blank=True, null=True)
    # ship_via = models.ForeignKey(Shipper, on_delete=models.SET_NULL, null=True)
    freight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ship_name = models.CharField(max_length=100)
    # ship_address = models.CharField(max_length=200)
    # ship_city = models.CharField(max_length=50)
    # ship_region = models.CharField(max_length=50, blank=True, null=True)
    # ship_postal_code = models.CharField(max_length=20, blank=True, null=True)
    # ship_country = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.id}"


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    discount = models.FloatField()

    def __str__(self):
        return f"{self.order.id} - {self.product.product_name}"


class CustomerDemographic(models.Model):
    customer_desc = models.TextField()

    def __str__(self):
        return self.customer_desc[:30]


class CustomerCustomerDemo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_type = models.ForeignKey(CustomerDemographic, on_delete=models.CASCADE)

