from django.db import models


class CustomerDetails(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_username = models.CharField(max_length=100, blank=True, null=True)
    customer_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    mobileno = models.BigIntegerField(blank=True, null=True)
    customer_password = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_details'


class CustomerQuery(models.Model):
    customer = models.ForeignKey(CustomerDetails, models.DO_NOTHING)
    customer_name = models.CharField(max_length=20)
    customer_email = models.CharField(max_length=60)
    customer_number = models.CharField(max_length=11)
    customer_message = models.CharField(max_length=100)
    employee_reply = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'customer_query'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HotelBooking(models.Model):
    customer = models.ForeignKey(CustomerDetails, models.DO_NOTHING)
    customer_name = models.CharField(max_length=40)
    customer_email = models.CharField(max_length=40)
    customer_number = models.CharField(max_length=11)
    room_booked = models.CharField(max_length=3)
    no_of_people = models.CharField(max_length=3)
    hotel_checkin = models.DateField()
    hotel_checkout = models.DateField()
    date_booked = models.DateField()
    hotel_status = models.IntegerField(db_comment='0 = Approve\r\n1 = Initialise\r\n2 = Denied')

    class Meta:
        managed = False
        db_table = 'hotel_booking'


class Payment(models.Model):
    paid_date = models.DateField(blank=True, null=True)
    paid_amount = models.FloatField(blank=True, null=True)
    paid_status = models.IntegerField()
    paid_by = models.IntegerField(blank=True, null=True)
    tour_id = models.IntegerField()


    class Meta:
        managed = False
        db_table = 'payment'


class TourRegistration(models.Model):
    customer = models.ForeignKey(CustomerDetails, models.DO_NOTHING)
    customer_name = models.CharField(max_length=30)
    customer_email = models.CharField(max_length=60)
    customer_phone = models.CharField(max_length=12)
    customer_address = models.CharField(max_length=100)
    customer_gender = models.CharField(max_length=8)
    customer_country = models.CharField(max_length=20)
    customer_state = models.CharField(max_length=20)
    customer_passport = models.CharField(unique=True, max_length=10)
    customer_selected_package = models.IntegerField()
    trip_startdate = models.DateField()
    trip_enddate = models.DateField()
    trip_amt = models.FloatField()
    customer_payment = models.FloatField()
    trip_status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tour_registration'


class TourismPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    plan_name = models.CharField(max_length=40, blank=True, null=True)
    plan_details = models.CharField(max_length=200, blank=True, null=True)
    plan_duration = models.CharField(max_length=100, blank=True, null=True)
    plan_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tourism_plan'


class TrsEmployee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    emp_address = models.CharField(max_length=100)
    emp_dob = models.DateField()
    emp_email = models.CharField(max_length=200)
    emp_mobno = models.BigIntegerField()
    emp_sal = models.FloatField()
    emp_type = models.IntegerField()
    emp_username = models.CharField(max_length=100)
    emp_password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'trs_employee'


class VehicleRegistration(models.Model):
    customer = models.ForeignKey(CustomerDetails, models.DO_NOTHING)
    customer_name = models.CharField(max_length=50)
    customer_license = models.CharField(unique=True, max_length=16)
    customer_email = models.CharField(max_length=60)
    customer_phone = models.CharField(max_length=11)
    customer_pickup = models.DateField()
    customer_drop = models.DateField()
    vehicle_type = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    amount = models.FloatField()
    vehicle_status = models.IntegerField(db_comment='0 = Approve\r\n1 = Initialise\r\n2 = Denied')

    class Meta:
        managed = False
        db_table = 'vehicle_registration'
