from ast import Not
from asyncio.windows_events import NULL
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date

# Create your models here.

# Models are for database management

# Anytime there's a change in the models.py, the 'python manage.py makemigrations' needs to be executed. 
# Followed by 'python manage.py migrate', to send all the changes to the database

# An admin user needs to be created. It can be created using the 'python manage.py createsuperuser' command

# The admin for this one is 'admin', '12345678'

# When using the 'models.Model', it changes the class to a database

class SalesManager(BaseUserManager):
    def add_sale(self, type, price, username):
        '''Add a new sale to the Sales class'''

        sale = self.model(
            type = type,
            price = price,
            username = username
        )

        sale.save()

class Sales(AbstractBaseUser):
    today = date.today()

    todayDate = today.strftime("%Y-%m-%d")

    type = models.CharField(max_length = 7, null = True, blank = True)
    price = models.CharField(max_length = 45, null = True, blank = True)
    date = models.DateTimeField(verbose_name = "date created", default = todayDate)    # Set the current date by default
    username = models.CharField(max_length = 30, null = True, blank = True)

    objects = SalesManager()