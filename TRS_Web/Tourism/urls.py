from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('log-out',views.logOut,name='log-out'),
    path('register_page', views.register, name='register_page'),
    path('login_page', views.login, name='login_page'),
    path('home', views.login_check, name='home'),
    path('registered', views.registered_check, name='registered'),
    path('tour_page', views.tour_page, name='tour_page'),
    path('tour_registration', views.tour_register, name="tour_registration"),
    path('vehicle_page', views.vehicle_page,name='vehicle_page'),
    path('vehicle_register', views.vehicle_registration, name='vehicle_register'),
    path('customer_contact', views.customer_contact, name='customer_contact'),
    path('hotel_book',views.hotel_booked,name='hotel_book'),
    path('hotel',views.hotel_book,name='hotel'),
    path('recommend',views.recommed,name="recommend"),
    path('orders',views.customer_orders,name='orders'),
    path('update-tour/(<int:plan_id>)',views.updateTour,name='update-tour'),
    path('delete-tour/(<int:tour_id>)',views.delete_tour,name='delete-tour'),
]
