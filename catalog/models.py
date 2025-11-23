from django.db import models
from django.utils.text import slugify

# --------------------------
# CATEGORY
# --------------------------
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته")
    slug = models.SlugField(unique=True, blank=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# --------------------------
# BRAND
# --------------------------
class Brand(models.Model):
    name = models.CharField(max_length=200, verbose_name="برند")
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


# --------------------------
# PRODUCT
# --------------------------
class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name="نام محصول")
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.SET_NULL, related_name="products")

    price = models.PositiveIntegerField(verbose_name="قیمت")
    discount_price = models.PositiveIntegerField(null=True, blank=True, verbose_name="قیمت با تخفیف")
    stock = models.PositiveIntegerField(default=0, verbose_name="موجودی")

    short_description = models.CharField(max_length=500, blank=True, verbose_name="توضیحات کوتاه")
    description = models.TextField(blank=True, verbose_name="توضیحات کامل")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"

    def __str__(self):
        return self.title

    @property
    def final_price(self):
        return self.discount_price if self.discount_price else self.price

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


# --------------------------
# PRODUCT IMAGES (Gallery)
# --------------------------
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/')
    is_main = models.BooleanField(default=False, verbose_name="تصویر اصلی؟")

    class Meta:
        verbose_name = "تصویر محصول"
        verbose_name_plural = "تصاویر محصول"

    def __str__(self):
        return f"تصویر {self.product.title}"


# --------------------------
# PRODUCT ATTRIBUTES (like Digikala)
# --------------------------
class ProductAttribute(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان ویژگی")

    class Meta:
        verbose_name = "ویژگی"
        verbose_name_plural = "ویژگی‌ها"

    def __str__(self):
        return self.title


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, related_name='attributes', on_delete=models.CASCADE)
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=300)

    class Meta:
        verbose_name = "مقدار ویژگی"
        verbose_name_plural = "مقادیر ویژگی"

    def __str__(self):
        return f"{self.attribute.title}: {self.value}"
