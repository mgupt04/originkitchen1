from django.db import models
from django.utils import timezone

class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('appetizers', 'Appetizers'),
        ('soups_salads', 'Soups & Salads'),
        ('mains', 'Mains'),
        ('sides', 'Sides'),
        ('desserts', 'Desserts'),
        ('drinks', 'Drinks'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    calories = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class CartItem(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"

class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    hours = models.TextField()
    map_embed_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    num_guests = models.PositiveIntegerField(
        choices=[(i, str(i)) for i in range(1, 10)]
    )
    reservation_time = models.DateTimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation for {self.full_name} on {self.reservation_time} at {self.location.name}"

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    preview = models.TextField(max_length=500)
    image = models.ImageField(upload_to='blog_images/')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_posted']

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

    class Meta:
        ordering = ['-submitted_at']

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.created_at}"

    class Meta:
        ordering = ['-created_at']

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=100)
    item_price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} x {self.item_name} (Order #{self.order.id})"