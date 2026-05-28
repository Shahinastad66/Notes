from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):

    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name="بیوگرافی")
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="شماره تلفن")
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True, verbose_name="عکس پروفایل")
    birth_date = models.DateField(blank=True, null=True, verbose_name="تاریخ تولد")
    
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
    
    def __str__(self):
        return self.username