from django.urls import path
from . import views

urlpatterns =[
    path('home',views.home,name='home'),
    path('',views.login,name='login'),
    path('booking',views.booking,name='booking'),
    path('auth',views.login_check,name='auth'),
    path('log-out',views.logout,name='log-out'),
    path('package',views.package,name='package'),
    path('add-package',views.add_package,name='add-package'),
    path('employee',views.employee,name='employee'),
    path('add-employee',views.add_employee,name='add-employee'),
    path('vehicle-details', views.vehicle_display,name ='vehicle-details'),
    path('hotel-details',views.hotel_details,name='hotel-details'),
    path('del-tour/(<int:mobno>)',views.deleted_tour,name="del-tour"),
    path('bill/(<int:cust_id>)',views.bill,name='bill'),
    path('approve-tour/<slug:pkg_id>/<int:custid>/<int:tour_id>',views.approve_tour,name='approve-tour'),
    path('approve-hotel/(<int:hotel_id>)',views.approve_hotel,name='approve-hotel'),
    path('deny-hotel/(<int:hotel_id>)',views.deny_hotel,name='deny-hotel'),
    path('approve-vehicle/(<int:vehicle_id>)',views.approve_vehicle,name='approve-vehicle'),
    path('deny-vehicle/(<int:vehicle_id>)',views.deny_vehicle,name='deny-vehicle'),
    path('tour-report',views.tourreport,name='tour-report'),
    path('vehicle-report',views.vehiclereport,name='vehicle-report'),
    path('hotel-report',views.hotelreport,name='hotel-report'),

]