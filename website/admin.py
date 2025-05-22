from django.contrib import admin
from .models import ContactMessage, MenuItem, CartItem, Location, Reservation, Blog, Order, OrderItem

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submitted_at')
    list_filter = ('submitted_at',)
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'submitted_at'
    ordering = ('-submitted_at',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'created_at')
    search_fields = ('name', 'address')
    list_filter = ('created_at',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'num_guests', 'reservation_time', 'location')
    list_filter = ('reservation_time', 'location')
    search_fields = ('full_name', 'email', 'location__name')
    date_hierarchy = 'reservation_time'
    ordering = ('-reservation_time',)

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'calories')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    ordering = ('name',)

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('menu_item', 'quantity')
    search_fields = ('menu_item__name',)
    ordering = ('menu_item',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_posted')
    list_filter = ('date_posted',)
    search_fields = ('title', 'content', 'preview')
    date_hierarchy = 'date_posted'
    ordering = ('-date_posted',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id',)
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'item_name', 'item_price', 'quantity')
    list_filter = ('order',)
    search_fields = ('item_name',)
    ordering = ('order',)