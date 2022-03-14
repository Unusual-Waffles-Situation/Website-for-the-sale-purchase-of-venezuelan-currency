from lib2to3.pytree import Base
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from datetime import date

# Create your models here.

# Admin user is admin/12345678

# Beepo is Beepo@gmail.com/123456789

'''
    To create a custom user model, the AbstractBaseUser has to be entextend
    This has to be added to the settings.py "AUTH_USER_MODEL = 'APP_NAME.CUSTOM_USER_MODEL_NAME' (eg. user.User in this case)"
    The date_joined, last_login and all the boolean attributes has to be added by default, as
    the base Django User has to be expanded using this attributes on the custom user model
'''

class UserManager(BaseUserManager):

    def create_user(self, email, username, password = None):
        '''Function to create a new user.'''
        
        # This function has to be overrided, as it's a default Django user function

        if not email:
            raise ValueError("Los usuarios deben tener un correo electronico")

        elif not username:
            raise ValueError("Los usuarios deben tener un nombre de usuario")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, username, password):
        '''Creates a new superuser'''

        # This function has to be overrided, as it's a default Django user function

        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password, 
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True

        user.save()

        return user


class User(AbstractBaseUser):
    today = date.today()

    todayDate = today.strftime("%Y-%m-%d")

    username = models.CharField(max_length = 30, unique = True)
    email = models.EmailField(verbose_name = "email", max_length = 60, unique = True)
    password = models.CharField(max_length = 40)
    date_joined = models.DateField(verbose_name = "date joined", default = todayDate)
    last_login = models.DateField(verbose_name = "last login", default = todayDate)
    is_admin = models.BooleanField(default = False)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)

    objects = UserManager()

    USERNAME_FIELD = 'email'    # Default log in attribute. The default one is the username
    REQUIRED_FIELDS = ['username']    # Required field to create a new user

    # All this functions has to be added by default to the custom user model
    def __str__(self):
        '''Default return value (username)'''

        return str(self.username)

    def has_perm(self, perm, obj = None):
        '''Check if the user has permissions/is admin'''

        return self.is_admin

    def has_module_perms(self, app_label):
        '''Returns true if the user has module permission, which by default is true'''

        return True