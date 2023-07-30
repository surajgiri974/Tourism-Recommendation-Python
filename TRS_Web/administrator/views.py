from urllib.request import HTTPRedirectHandler
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from Tourism.models import *
from django.db import connection
from django.contrib import messages

# Create your views here.

def tourreport(request):
    query = 'SELECT * From tour_registration,tourism_plan where tour_registration.customer_selected_package = tourism_plan.plan_id;'
    data = TourRegistration.objects.raw(query)
    context ={
        'tour_data' : data,
    }
    return render(request,'administrator/report.html',context)
def hotelreport(request):
    data = HotelBooking.objects.all()
    context ={
        'hotel_data' : data,
    }
    return render(request,'administrator/report.html',context)
def vehiclereport(request):
    data = VehicleRegistration.objects.all()
    context ={
        'vehicle_data' : data,
    }
    return render(request,'administrator/report.html',context)


def login(request):
    return render(request,'administrator/login.html')

def bill(request,cust_id):
    tour = TourRegistration.objects.get(id = cust_id)
    payment = Payment.objects.get(tour_id = cust_id)
    plan = TourismPlan.objects.get(plan_id = tour.customer_selected_package )
    context = {
        'invoice_number' : payment.id,
        'invoice_date'   : payment.paid_date,
        'customer_name'  : tour.customer_name,
        'customer_address' : tour.customer_address,
        'customer_phone'  : tour.customer_phone,
        'package_name'   : plan.plan_name,
        'trip_duration'  : plan.plan_duration,
        'total_amount'   : payment.paid_amount,
        'description'    : plan.plan_details,
        'payment_status' : payment.paid_status

    }
    return render(request,'administrator/bill.html',context)


def login_check(request):
    try:
        employee_id = request.POST.get('email')
        employee_pw = request.POST.get('password')
        if employee_id == '' and employee_pw == '':
            messages.warning(request, 'Fields Are Empty !!')
            return render(request, 'administrator/login.html')
        else:
            login  = TrsEmployee.objects.get(emp_username=employee_id,emp_password=employee_pw)
            print(login)
            messages.add_message(request,messages.SUCCESS, 'Login Successfully!!')
            request.session['admin_username'] = employee_id
            emps_type = TrsEmployee.objects.get(emp_username=employee_id)
            print(emps_type.emp_type)
            return HttpResponseRedirect("/Tour-Master/home",{'username':request.session['admin_username'],'emp_status':emps_type.emp_type})
    except TrsEmployee.DoesNotExist:
        messages.add_message(request,messages.SUCCESS,"Login Failed !!")
        return HttpResponseRedirect("/Tour-Master/")

def logout(request):
    try:
        request.session.flush()
        return HttpResponseRedirect('/Tour-Master/')
    except:
        return HttpResponse("<h1>ERROR</h1>")

def home(request):
    cursor = connection.cursor()
    total_tour_booking=TourRegistration.objects.count()
    total_hotel_booking=HotelBooking.objects.count()
    total_vehicle_booking=VehicleRegistration.objects.count()
    total_payment = Payment.objects.count()
    context = {
       'tour_count':total_tour_booking,
       'hotel_count':total_hotel_booking,
       'total_vehicle':total_vehicle_booking,
       'total_payment':total_payment,
    }
    
    return render(request,'administrator/index.html',context)

def booking(request):
    booked = TourRegistration.objects.raw("select * from tour_registration where trip_status = 1 ")
    booked_completed = TourRegistration.objects.raw("select * from tour_registration where trip_status = 2 ")
    cancelled = TourRegistration.objects.raw("select * from tour_registration where trip_status = 3")
    return render(request,'administrator/orders.html',{'booked':booked,'completed':booked_completed,'cancelled':cancelled})

def package(request):
    return render(request,'administrator/package.html')

def add_package(request):
    if request.POST:
        tour_name = request.POST['package_name']
        tour_amount = request.POST['package_amount']
        tour_duration = request.POST['package_duration']
        tour_details = request.POST['package_details']
        Package = TourismPlan(plan_name = tour_name,
                            plan_details = tour_details,
                            plan_duration = tour_duration,
                            plan_amount = tour_amount)
        Package.save()
        messages.add_message(request,messages.SUCCESS,"Package Added Successfully !!")
        import time
        time.sleep(3)
        return HttpResponseRedirect("/Tour-Master/package")
    else:
        messages.add_message(request,messages.ERROR,"Failed For Some Reason !!")
        return HttpResponseRedirect("/Tour-Master/package")
    

def vehicle_display(request):
    record = VehicleRegistration.objects.all()
    return render(request,'administrator/vehicle_display.html',{'record':record})

def deleted_tour(request,mobno):
    regDel = TourRegistration.objects.get(id = mobno) 
    regDel.delete()
    messages.add_message(request,messages.SUCCESS,"Customer Data Deleted !!")
    return HttpResponseRedirect("/Tour-Master/booking")

def approve_tour(request,pkg_id,custid,tour_id):
    import datetime
    trip_amt = TourismPlan.objects.get(plan_id = pkg_id)
    customer = CustomerDetails.objects.get(customer_id = custid)
    tour = TourRegistration.objects.get(id = tour_id)
    tour.trip_status = 2
    tour.save()
    appCust = Payment(
        paid_date = datetime.datetime.now(),
        paid_amount =  trip_amt.plan_amount,
        paid_status = 0,
        paid_by = customer.customer_id,
        tour_id = tour_id
    )
    appCust.save()
    return HttpResponseRedirect("/Tour-Master/booking")
def hotel_details(request):
    record = HotelBooking.objects.all()
    return render(request,'administrator/hotel_details.html', {'record':record})
def approve_hotel(request,hotel_id):
    hotel = HotelBooking.objects.get(id = hotel_id)
    hotel.hotel_status = 0
    hotel.save()
    return HttpResponseRedirect('/Tour-Master/Hotel-details')
def deny_hotel(request,hotel_id):
    hotel = HotelBooking.objects.get(id = hotel_id)
    hotel.delete()
    return HttpResponseRedirect('/Tour-Master/hotel-details')
def approve_vehicle(request,vehicle_id):
    vehicle = VehicleRegistration.objects.get(id = vehicle_id)
    vehicle.vehicle_status = 0
    vehicle.save()
    return HttpResponseRedirect('/Tour-Master/vehicle-details')
def deny_vehicle(request,vehicle_id):
    vehicle = VehicleRegistration.objects.get(id = vehicle_id)
    vehicle.delete()
    return HttpResponseRedirect('/Tour-Master/vehicle-details')

def employee(request):
    return render(request,'administrator/register_employee.html')

def add_employee(request):
    if request.POST:
        emp_name = request.POST['firstname'] + " "+request.POST['lastname']
        emp_address = request.POST['address']
        emp_dob = request.POST['dob']
        emp_email = request.POST['email']
        emp_phone = request.POST['phone']
        emp_sal =  request.POST['salary']
        emp_type = request.POST['emp_type']
        emp_username = request.POST['username']
        emp_password = request.POST['password']
        employee = TrsEmployee(
            emp_name = emp_name,
            emp_address = emp_address,
            emp_dob =  emp_dob,
            emp_email = emp_email,
            emp_mobno = emp_phone,
            emp_sal = emp_sal,
            emp_type = emp_type,
            emp_username = emp_username,
            emp_password = emp_password
        )
        employee.save()
        messages.add_message(request,messages.SUCCESS,"Employee Added Successfully !!")
        return HttpResponseRedirect("/Tour-Master/employee")
    else:
        return HttpResponseRedirect("/Tour-Master/employee")