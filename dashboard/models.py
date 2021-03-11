from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class TicketSells(models.Model):
    class Meta:
        verbose_name = 'Ticket Sells'
        verbose_name_plural = 'Ticket Sells'
    TYPES = (
       ('single', 'single ticket'),
       ('monthly', 'monthly ticket'),
       ('other', 'other ticket'),
   )
    date = models.DateField()
    ticket_type = models.CharField(max_length=32, choices=TYPES,default=None)
    ticket_count = models.IntegerField()
    

class Survey(models.Model):
    GENDER_CHOICES = (
       ('male', 'Male'),
       ('female', 'Female'),
       #('diverse','Diverse'),
   )
    SALARY_CHOICES = (
       ('<500','Less than €500'),
       ('>500&<1000','Between €500 and €1000'),
       ('>1000&<2000','Between €1000 and €2000'),
       ('>2000','More than €2000'),
   )
    NO = 0
    YES = 1
    BOOLEAN_CHOICES = (
        (NO,'No'),
        (YES,'Yes'),
    )
    age = models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)])
    gender = models.CharField(max_length=32,choices=GENDER_CHOICES)
    income = models.CharField(max_length=32,choices=SALARY_CHOICES)
    ownCar = models.IntegerField(choices=BOOLEAN_CHOICES)
    usePT = models.IntegerField(choices=BOOLEAN_CHOICES)
    ptUsageStartDate = models.DateField()

    #class PTusage(models.Model):
    #   


    
    
