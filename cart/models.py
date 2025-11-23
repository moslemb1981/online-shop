from django.db import models
from django.contrib.auth.models import User
from catalog.models import Product


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True,
        related_name="cart"
    )
    session_key = models.CharField(
        max_length=40, blank=True, null=True,
        help_text="برای کاربران غیرعضو"
    )
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبدهای خرید"

    def __str__(self):
        if self.user:
            return f"سبد خرید {self.user.username}"
        return f"سبد خرید مهمان ({self.session_key})"

    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())

    @property
    def total_price(self):
        return sum(item.total_price for item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, related_name="items", on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        Product, related_name="cart_items", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(default=1)
    price_at_time = models.PositiveIntegerField(
        help_text="قیمت محصول در لحظه اضافه شدن به سبد"
    )

    class Meta:
        verbose_name = "آیتم سبد خرید"
        verbose_name_plural = "آیتم‌های سبد خرید"

    def __str__(self):
        return f"{self.product.title} × {self.quantity}"

    @property
    def total_price(self):
        return self.quantity * self.price_at_time
