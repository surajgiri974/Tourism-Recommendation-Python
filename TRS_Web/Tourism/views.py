from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.db import connection
from django.contrib import messages
import js2py, datetime
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import send_mail
from .models import *
import time

# Create your views here.

def home(request):
    return render(request, 'Tourism/index.html')

def login(request):
    return render(request, 'Tourism/login.html')

def register(request):
    return render(request, 'Tourism/login.html')

def customer_orders(request):
    try:
        username = request.session['username']
        customer = CustomerDetails.objects.get(customer_username = username)
        query = "select * from tourism_plan,tour_registration where tour_registration.customer_selected_package = tourism_plan.plan_id AND tour_registration.customer_id = %s" % customer.customer_id
        tour_register = TourRegistration.objects.raw(query)
        hotel_booked = HotelBooking.objects.filter(customer_id=customer.customer_id,).all()
        vehicle_booked = VehicleRegistration.objects.filter(customer_id=customer.customer_id)
        profile = CustomerDetails.objects.get(customer_id=customer.customer_id)
        plans = TourismPlan.objects.all()

        context = {
            'tour_booked' : tour_register,
            'hotel_booked' : hotel_booked ,
            'vehicle_booked' : vehicle_booked , 
            'profile' : profile,
            'plans' : plans,
        }
        return render(request,"Tourism/customer_orders.html",context)
    except KeyError:
        return HttpResponse("<h1>Please Log in </h1><a href='/'>Click Here to Log in</a> ")

def updateTour(request,plan_id):
    startDate =  request.POST['startdate']
    endDate =  request.POST['enddate']
    planed_id = request.POST['plan_id']
    tour = TourRegistration.objects.get(id=plan_id)
    tour.trip_startdate = startDate
    tour.trip_enddate = endDate
    tour.save()
    messages.add_message(request,messages.SUCCESS,"Tour Package Updated")
    return HttpResponseRedirect("/orders")


def registered_check(request):
    custName = request.POST['custname']
    username = request.POST['username']
    email = request.POST['email']
    mobileno = request.POST['mobileno']
    pw = request.POST['pw']
    pw1 = request.POST['pw1']

    if pw != pw1:
        messages.add_message(request,messages.ERROR,"Password Does not Match")
    else:
        csave = CustomerDetails(
            customer_username=username,
            customer_name=custName,
            email = email,
            mobileno=mobileno,
            customer_password=pw
        )
        csave.save()
        msg=custName+", \nThank You For Registering with Us !!\nRegard,\nTRS Team"
        send_mail("Welcome to Tourism Booking",msg,'sachinkalloli932@gmail.com',[email])
        messages.add_message(request,messages.SUCCESS,"Registered Sucessfully !!")
        return HttpResponseRedirect("/")

def delete_tour(request,tour_id):
    tour = TourRegistration.objects.get(id = tour_id)
    tour.delete()
    messages.add_message(request,messages.SUCCESS,"Tour Deleted Successfully")
    return HttpResponseRedirect('/orders')




def login_check(request):
    try:
        customer_id = request.POST.get('useremail')
        customer_pw = request.POST.get('userpw')
        if customer_id == '' and customer_pw == '':
            messages.warning(request, 'Fields Are Empty !!')
            return render(request, 'Tourism/index.html')
        else:
            login  = CustomerDetails.objects.get(customer_username=customer_id,customer_password=customer_pw)
            con = connection.cursor()
            messages.add_message(request,messages.SUCCESS, 'Login Successfully!!')
            request.session['username'] = customer_id   
            return render(request, 'Tourism/index.html')
    except CustomerDetails.DoesNotExist:
        messages.add_message(request,messages.ERROR,"Login Failed !!")
        return HttpResponseRedirect("/")

def tour_page(request):
    plans = TourismPlan.objects.all()
    return render(request, 'Tourism/Tour_Register_new.html',{'plan':plans})


def tour_register(request):
    cfname = request.POST.get('data_3', False)
    clname = request.POST.get('data_4', False)
    cname = str(cfname) + ' ' + str(clname)
    cemail = request.POST.get('data_5', False)
    cphone = request.POST.get('data_6', False)
    caddress = request.POST.get('data_18', False)
    cgender = request.POST.get('data_20', False)
    ccountry = request.POST.get('data_15', False)
    cstate = request.POST.get('data_16', False)
    cpassport = request.POST.get('data_19', False)
    cpackage = request.POST.get('data_21', False)
    cSelectdate = request.POST.get('data_22', False)
    print(cname, cemail, cphone, caddress, cgender, ccountry, cstate, cpassport, cpackage, cSelectdate)
    con = CustomerDetails.objects.get(customer_username=request.session['username'])
    trip_amt = TourismPlan.objects.get(plan_id = cpackage)
    print(trip_amt.plan_amount)
    tour = TourRegistration(
        customer_id = con.customer_id,
        customer_name = cname,
        customer_email = cemail,
        customer_phone = cphone,
        customer_address = caddress,
        customer_gender = cgender,
        customer_country = ccountry,
        customer_state = cstate,
        customer_passport = cpassport,
        customer_selected_package = cpackage,
        trip_startdate = cSelectdate,
        trip_enddate = '2000-10-01',
        trip_amt = trip_amt.plan_amount,
        customer_payment = 0,
        trip_status = 1
    )
    tour.save()
    messages.add_message(request, messages.SUCCESS,'Successfully Registered')
    return render(request, 'Tourism/thanks.html')


def vehicle_page(request):
    return render(request, 'Tourism/vehicle_booking.html')


def vehicle_registration(request):
    try:
        username = request.POST['rental_user_name']
        userdl = request.POST['rental_user_dl']
        vtype = request.POST['vehicle_type']
        useremail = request.POST['rental_user_email']
        userphone = request.POST['rental_user_phone']
        pickup = request.POST['rental_user_pickD']
        drop = request.POST['rental_user_dropD']
        city = request.POST['city']
        amt = request.POST['vamt']
        print(username, userdl, useremail, userphone, vtype, pickup, drop, city, amt)
        q = 'INSERT INTO `vehicle_registration`(`id`, `customer_id`,`customer_name`, `customer_license`, `customer_email`, ' \
            '`customer_phone`, `customer_pickup`, `customer_drop`, `vehicle_type`, `city`, `amount`,`vehicle_status`) VALUES (%s,%s,%s,%s,' \
            '%s,%s,%s,%s,%s,%s,%s,%s) '
        con = CustomerDetails.objects.get(customer_username=request.session['username'])
        v = (0,con.customer_id,username, userdl, useremail, userphone, pickup, drop, vtype, city, amt,1)
        cursor = connection.cursor()
        cursor.execute(q, v)
        messages.success(request, 'Confirmation Will be sent Soon')
        return render(request, 'Tourism/thanks.html')

    except:
        messages.success(request, 'Something Went Wrong')
        return render(request, 'Tourism/vehicle_booking.html')


def customer_contact(request):
    name = request.POST['name']
    cemail = request.POST['cemail']
    cnumber = request.POST['cnumber']
    cmsg = request.POST['cmsg']
    print(name, cemail, cnumber, cmsg)
    q = "INSERT INTO `customer_query`(`customer_name`, `customer_email`, `customer_number`, `customer_message`, " \
        "`employee_reply`) VALUES (%s,%s,%s,%s,%s) "
    v = (name, cemail, cnumber, cmsg, '')
    cursor = connection.cursor()
    cursor.execute(q, v)
    messages.success(request, 'Thank You For Enquiry!!') 
    send_mail('Thank You for Contacting Us !', 'We Will Reach out to you Soon!!', 'pavanshinde678@gmail.com', (cemail,), fail_silently=False)   
    return render(request, 'Tourism/thanks.html')

def logOut(request):
    request.session.flush()
    return HttpResponseRedirect("/")

def recommed(request):
    return render(request, 'Tourism/recommed.html')


def hotel_book(request):
    return render(request, 'Tourism/hotel_booking.html')
    
def hotel_booked(request):
    from datetime import date
    d=date.today()
    name = request.POST.get('custname')
    cemail = request.POST.get('cemail')
    cnumber = request.POST.get('cnumber')
    roombkd= request.POST.get('roombkd')
    people=request.POST.get('people')
    checkin=request.POST.get('checkindt')
    checkout=request.POST.get('checkoutdt')
    print(name,cemail,cnumber,roombkd,people,checkin,checkout)
    con = CustomerDetails.objects.get(customer_username=request.session['username'])
    hotel = HotelBooking(
        customer_id = con.customer_id,
        customer_name = name,
        customer_email = cemail,
        customer_number = cnumber,
        room_booked = roombkd,
        no_of_people = people,
        hotel_checkin = checkin,
        hotel_checkout = checkout,
        date_booked = d ,
        hotel_status = 1,
    )
    hotel.save()
    messages.success(request, 'Thank You For Hotel Booking We Will Reach Out to You Soon!!')
    return render(request, 'Tourism/index.html')
