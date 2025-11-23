from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    phone_number = models.CharField(max_length=20, blank=True, verbose_name="شماره موبایل")
    national_code = models.CharField(max_length=10, blank=True, verbose_name="کد ملی")

    # آدرس پیش‌فرض برای سفارش
    default_address = models.ForeignKey(
        "Address",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="default_for_user"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "پروفایل کاربر"
        verbose_name_plural = "پروفایل کاربران"

    def __str__(self):
        return self.user.username


class Address(models.Model):
    user = models.ForeignKey(User, related_name="addresses", on_delete=models.CASCADE)

    full_name = models.CharField(max_length=255, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=20, verbose_name="شماره تماس")
    province = models.CharField(max_length=100, verbose_name="استان")
    city = models.CharField(max_length=100, verbose_name="شهر")
    postal_address = models.TextField(verbose_name="نشانی کامل")
    postal_code = models.CharField(max_length=10, verbose_name="کد پستی")

    is_active = models.BooleanField(default=True, verbose_name="فعال؟")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "آدرس"
        verbose_name_plural = "آدرس‌های کاربر"

    def __str__(self):
        return f"{self.full_name} - {self.city}"
