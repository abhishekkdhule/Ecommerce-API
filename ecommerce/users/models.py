from django.db import models
from core.models import Address
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, name, contact_number, password=None):
        if email is None:
            raise TypeError("User must have email")
        if password is None:
            raise TypeError("Password cannot be None")
        user: User = self.model(email=self.normalize_email(email), name=name, contact_number=contact_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email=email, password=password, name='', contact_number=None)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user
        


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    contact_number = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['email', 'name']
    objects = UserManager()

    def __str__(self) -> str:
        return self.email
        

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")
    points = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.email


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller")
     
    def __str__(self) -> str:
        return self.user.email


