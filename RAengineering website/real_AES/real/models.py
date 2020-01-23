from django.db import models

# Create your models here.
class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


class Inquiry(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=200, default="")
    title = models.CharField(max_length=200,default="")
    company = models.CharField(max_length=200, default="")
    address = models.CharField(max_length=200, default="")
    city = models.CharField(max_length=200, default="")
    state = models.CharField(max_length=200, default="")
    zip_code = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=100, default="")

class Client(models.Model):
    client_id = models.AutoField
    client_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='images', default="")

    def __str__(self):
        return self.client_name