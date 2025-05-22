# simplygreen/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from website import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reservation/', views.reservation, name='reservation'),
    path('reservation/success/', views.reservation_success, name='reservation_success'),
    path('documentation/', views.documentation, name='documentation'),
    path('menu/', views.menu, name='menu'),
    path('cart/', views.cart, name='cart'),
    path('cart/add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/increase/<int:item_id>/', views.increase_cart_item, name='increase_cart_item'),
    path('cart/decrease/<int:item_id>/', views.decrease_cart_item, name='decrease_cart_item'),
    path('place-order/', views.place_order, name='place_order'),
    path('order-success/', views.order_success, name='order_success'),
    path('book-reservation/', views.book_reservation, name='book_reservation'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('contact/', views.contact, name='contact'),
    path('locations/', views.locations, name='locations'),
    path('sustainability/', views.sustainability, name='sus'),
    path('plastic/', views.p, name='p'),
    path('upcycle/', views.u, name='u'),
    path('water/', views.w, name='w'),
    path('energy/', views.e, name='e'),
    path('local/', views.l, name='l'),
    path('food/', views.f, name='f'),
    path('chefcurate/', views.m, name='m'),
    path('sustain/', views.n, name='n'),
    path('farmfreshmore/', views.o, name='o'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
