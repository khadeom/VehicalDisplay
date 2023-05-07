from django.db import models
from datetime import date, datetime

# Create your models here.



class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    vehical
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):
    model = models.CharField(max_length=100)
    number = models.CharField(max_length=100)
    seat_capacity = models.PositiveIntegerField()
    rent_per_day =  models.DecimalField(max_digits=8,decimal_places=2)
    is_avaliable = models.BooleanField(default=True)
    agency = models.ForeignKey('VehicalAgencie', on_delete=models.CASCADE)

    def __str__(self):
        return self.model

    def is_rented(self):
        return self.is_avaliable is not True

    def rent(self):
        if self.is_available:
            self.is_available = False
            self.save()

    def return_vehicle(self):
        if not self.is_available:
            self.is_available = True
            self.save()

class VehicalAgencie(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer} booked {self.vehicle} from {self.start_date} to {self.end_date}"
