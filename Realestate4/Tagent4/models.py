from django.core.urlresolvers import reverse
from django.db import models
from .validations import *
class ContactInfo(models.Model):
    mobile_number= models.CharField(max_length=15)
    phone_number= models.CharField(max_length=15)
    email_id= models.EmailField()
class Media(models.Model):
    media_id=models.AutoField(primary_key=True)
    media_name= models.CharField(max_length=20)
    media_path= models.FileField(upload_to='documents/')
class Agent(ContactInfo,Media):
    agent_id= models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=20,validators=[validate_first_name])
    last_name= models.CharField(max_length=20,validators=[validate_last_name])
    age=models.IntegerField()
    education= models.CharField(max_length=50,validators=[validate_education])
    company_name=models.CharField(max_length=50)
    specialization= models.CharField(max_length=100,validators=[validate_specelization])
    experence=models.IntegerField()
    agent_notes=models.TextField()
def get_absolute_url(self):
        return reverse('agent-update', kwargs={'pk': self.pk})

class Location(models.Model):
    agent = models.ForeignKey(Agent)
    foreign_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)

class Address(models.Model):
    agent= models.ForeignKey(Agent)
    address_id= models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20,validators=[validate_city])
    state= models.CharField(max_length=20,validators=[validate_state])
    landmark= models.CharField(max_length=20,validators=[validate_landmark])
    pincode= models.IntegerField()


