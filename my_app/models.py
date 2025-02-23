from djongo import models

class Products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    contact = models.CharField(max_length=100, default="N/A")
    description = models.TextField(default="No description provided")
    location = models.URLField(default="https://example.com/default-location")
    product_image = models.ImageField(upload_to='image/', blank=True, default='image/Form_to_Home.jpeg')
    available_kg = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.product_name

class User(models.Model):
    username = models.CharField(max_length=100, default="default_username")
    email = models.EmailField(unique=True, default="example@example.com")
    password = models.CharField(max_length=100, default="password123")

    def __str__(self):
        return self.username

class Order(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    street_address = models.CharField(max_length=255, default="")
    city = models.CharField(max_length=100, default="")
    state = models.CharField(max_length=100, default="")
    postal_code = models.CharField(max_length=20, default="")
    contact_number = models.CharField(max_length=20, default="")
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_option = models.CharField(max_length=10, default="deliver")

    def __str__(self):
        return f"Order for {self.product.product_name} by {self.customer_name}"
