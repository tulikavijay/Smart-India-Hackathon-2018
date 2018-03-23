from django.db import models
from django.core.validators import RegexValidator


# Create your models here.
class Producer(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    nationality = models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17,blank=True) 
    email=models.CharField(max_length=100,default='')
    production_house = models.CharField(max_length=100)
    production_house_add = models.CharField(max_length=300)
    local_agent = models.CharField(max_length=100, blank=True, default='')
    local_agent_add =  models.CharField(max_length=300, blank=True, default='')
    passport_regex = RegexValidator(regex=r'^\+?1?\d{6,9}$', message="Passport is not valid")
    passport_no = models.CharField(validators=[passport_regex],max_length=10,blank=True)
    passport_validity = models.DateField(blank=True)

class Production(models.Model):
    producer = models.CharField(max_length=100,default='')
    film = models.CharField(max_length=100)  
    production_house = models.CharField(max_length=100,default='')
    production_house_address = models.CharField(max_length=300,default='')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17,default='')    
    local_line_producer = models.CharField(max_length=100, blank=True, default='')
    local_line_producer_address =  models.CharField(max_length=300, blank=True, default='')
    director = models.CharField(max_length=100)
    cinematographer = models.CharField(max_length=100)
    art_director= models.CharField(max_length=100)
    script = models.FileField(upload_to='scripts/')
    undertaking = models.FileField(upload_to='undertaking/',default='')
    shoot_timing = models.TimeField()
    shoot_start_date= models.DateField()
    shoot_end_date = models.DateField()
    location = models.CharField(max_length=100)