from django.db import models

# Create your models here.
class Booking(models.Model):
    order_id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=90, default="")
    email=models.CharField(max_length=111, default="")
    date = models.CharField(max_length=6, default="")
    time = models.CharField(max_length=10, default="")
    people=models.IntegerField(default=1)
    message= models.CharField(max_length=5000, default="")


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    subject = models.CharField(max_length=70, default="")
    message = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name