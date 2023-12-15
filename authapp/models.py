
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

# Create your models here.

class myaccountmanager(BaseUserManager):
    def create_user(self,name,email,country,phone_number,password=None):
        if not email:
            raise ValueError('user must have an email address')

        if not name:
            raise ValueError('user must have an username')

        
        user=self.model(
            email=self.normalize_email(email),
            name=name,
            country=country,
            phone_number=phone_number,

            # first_name=first_name,
            # last_name=last_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self,email,country,phone_number,name,password):
        user=self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
            country=country,
            phone_number=phone_number,

            # first_name=first_name,
            # last_name=last_name,
        )
        
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user







class Account(AbstractBaseUser):
    # first_name= models.CharField(max_length=50)
    # last_name=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=20,unique=True)
    date_of_birth=models.DateField(blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    zip_code=models.CharField(max_length=10,blank=True,null=True)
    address=models.CharField(max_length=50,blank=True,null=True)
    gender=models.CharField(max_length=10,blank=True,null=True)


    #required filed mendotory 

    date_joined=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_superadmin=models.BooleanField(default=False)
    

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name','country','phone_number']

    objects=myaccountmanager()
    def fullname(self):
        pass
    def __str__(self):
        return self.email
    

    def has_perm(self,perm,obj=None):
        return self.is_admin
    

    def has_module_perms(self,add_label):
        return True