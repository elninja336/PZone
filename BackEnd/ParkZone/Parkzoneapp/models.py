from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=100)
    phone = models.CharField(max_length=10)
    residence = models.CharField(null = True,max_length=50 )
    # password = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name}"


class ParkingLot(models.Model):
    CATEGORY_CHOICES = {
        "P":"PARMANENT",
        "T":"TEMPORARY"
    }
    AVAILABILITY_CHOICES ={
        "A":"AVAILABLE",
        "O":"OCCUPIED"
    }

    slotNumber = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, default="T",max_length=1)
    availability = models.CharField(choices=AVAILABILITY_CHOICES, default="A",max_length=1)
    price = models.IntegerField()

    def __str__(self):
        return f"Slot {self.slotNumber} is {self.cartegory}"


class Reservation(models.Model):
    STATUS_CHOICES = {
    "P":"PENDING",
    "C":"COMFIRMED",
    "X":"CENCELLED"
}

    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    parkingLot = models.ForeignKey(ParkingLot, on_delete = models.CASCADE)
    reservationDate = models.DateField(auto_now=True)
    startDate = models.DateField()
    endDate = models.DateField()
    status =models.CharField(choices=STATUS_CHOICES, default="P",max_length=1)

    def __str__(self):
        return f"Reservation {self.id} done by {self.Customer.name}"

