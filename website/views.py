from django.shortcuts import render, redirect
from .models import MenuItem, CartItem, Reservation, Blog, ContactMessage, Location, Order, OrderItem
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q

def home(request):
    latest_blogs = Blog.objects.all()[:2]  # Get the 2 most recent blog posts
    return render(request, 'website/home.html', {'latest_blogs': latest_blogs})

def about(request):
    return render(request, 'website/about.html')

def reservation_success(request):
    return render(request, 'website/reservation_success.html')

def reservation(request):
    locations = Location.objects.all()
    if request.method == 'POST':
        full_name = request.POST['full_name']
        email = request.POST['email']
        num_guests = request.POST['num_guests']
        reservation_time = request.POST['reservation_time']
        location_id = request.POST['location']

        try:
            location = Location.objects.get(id=location_id)
        except Location.DoesNotExist:
            messages.error(request, "Invalid location selected.")
            return redirect('reservation')
        
        Reservation.objects.create(
            full_name=full_name,
            email=email,
            num_guests=num_guests,
            reservation_time=reservation_time,
            location=location
        )
        messages.success(request, 'Reservation made successfully!')
        return redirect('reservation_success')
    
    return render(request, 'website/reservation.html', {'locations': locations})

def documentation(request):
    return render(request, 'website/documentation.html')


def menu(request):
    # Get search query and category from GET parameters
    search_query = request.GET.get('search', '')
    category = request.GET.get('category', '')

    # Base queryset
    items = MenuItem.objects.all()

    # Filter by search query (name or description)
    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )

    # Filter by category
    if category:
        items = items.filter(category=category)

    context = {
        'items': items,
        'search_query': search_query,
        'category': category,
    }
    return render(request, 'website/menu.html', context)


def cart(request):
    cart_items = CartItem.objects.all()
    total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
    return render(request, 'website/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def add_to_cart(request, item_id):
    menu_item = MenuItem.objects.get(id=item_id)
    cart_item, created = CartItem.objects.get_or_create(menu_item=menu_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart')

def increase_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def decrease_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def place_order(request):
    if request.method == 'POST':
        # Get cart items before clearing
        cart_items = CartItem.objects.all()
        if not cart_items:
            messages.error(request, 'Your cart is empty.')
            return redirect('cart')

        # Calculate total price and create order
        total_price = sum(item.menu_item.price * item.quantity for item in cart_items)
        order = Order.objects.create(total_price=total_price)

        # Save order items
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                item_name=item.menu_item.name,
                item_price=item.menu_item.price,
                quantity=item.quantity
            )

        # Clear the cart
        CartItem.objects.all().delete()
        messages.success(request, 'Your order has been placed successfully!')
        return redirect('order_success')

    return render(request, 'website/place_order.html')

def order_success(request):
    return render(request, 'website/thankyouscreen.html')

def book_reservation(request):
    return render(request, 'website/reservation.html')

def blog(request):
    blog_posts = Blog.objects.all()
    return render(request, 'website/blog.html', {'blog_posts': blog_posts})

def blog_detail(request, blog_id):
    post = Blog.objects.get(id=blog_id)
    paragraphs = post.content.split('\n')
    return render(request, 'website/blog_detail.html', {
        'post': post,
        'paragraphs': paragraphs})

def increase_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')

def decrease_cart_item(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            ContactMessage.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Thank you for your message! It has been saved, and we’ll get back to you soon.')
            return redirect('contact')
        except Exception as e:
            messages.error(request, 'There was an error saving your message. Please try again later.')
            return redirect('contact')

    return render(request, 'website/contact.html')

def locations(request):
    locations = Location.objects.all()
    return render(request, "website/locations.html", {'locations': locations})

def sustainability(request):
    return render(request, "website/sustainability.html")

def p(request):
    return render(request, "website/plastic_more.html")

def u(request):
    return render(request, "website/upcycle_more.html")

def w(request):
    return render(request, "website/water_more.html")

def e(request):
    return render(request, "website/energy_more.html")

def l(request):
    return render(request, "website/local_more.html")

def f(request):
    return render(request, "website/food_more.html")

def m(request):
    return render(request, "website/chefcurate_more.html")

def n(request):
    return render(request, "website/sustain_more.html")

def o(request):
    return render(request, "website/farmfreshmore_more.html")