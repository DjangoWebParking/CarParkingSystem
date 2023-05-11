from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, Group
from django.utils.html import escape, mark_safe
from django.urls import path, include
# Create your models here.

from django.contrib.auth.models import BaseUserManager


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user

#     def create_superuser(self, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    is_customer = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    token = models.UUIDField(default=uuid.uuid4, editable=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        if self.is_superuser:
            self.is_customer = False
            self.is_admin = True

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # quá chi là áp lực
        # Nếu user được đánh dấu là customer hoặc admin, thêm vào các group tương ứng
        if self.is_customer:
            group, created = Group.objects.get_or_create(name='Customer')
            if created:
                group.save(using='default')
            self.groups.add(group)
        if self.is_admin:
            group, created = Group.objects.get_or_create(name='Admin')
            if created:
                group.save(using='default')
            self.groups.add(group)
        # super(User, self).save(*args, **kwargs)        
    # class Meta:
    #     swappable = 'AUTH_USER_MODEL'


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, null=True, blank=True)
    avatar = models.ImageField(upload_to='avatar_images/', default='avatar_images/image.jpg')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    comment = models.TextField(max_length=5000, blank=True)
    register_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    reg_date = models.DateTimeField(auto_now_add=True)


class Car(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    car_model = models.CharField(max_length=100)
    car_color = models.CharField(max_length=100)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='cars', to_field='id')
    reg_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return self.license_plate

    def save(self, *args, **kwargs):
        if self.owner.user is not None:
            self.owner.user.is_customer = True
            self.owner.user.save()
        super(Car, self).save(*args, **kwargs)


class ParkingSlot(models.Model):
    PARKING_TYPES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large')
    )

    slot_number = models.IntegerField(unique=True)
    parking_type = models.CharField(max_length=1, choices=PARKING_TYPES)
    is_available = models.BooleanField(default=True)
    cost_per_day = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.get_parking_type_display()} slot {self.slot_number}"


class ParkingRecord(models.Model):
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    car_number = models.CharField(max_length=20)
    entry_time = models.DateTimeField(auto_now_add=True)
    exit_time = models.DateTimeField(blank=True, null=True)
    total_cost = models.IntegerField(null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
