from django.shortcuts import get_object_or_404, redirect
from catalog.models import Product
from .models import Cart, CartItem
from django.http import HttpResponse

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # سبد کاربر
    cart = request.user.cart

    # آیا قبلاً آیتم وجود دارد؟
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'price_at_time': product.price}
    )

    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart_detail")


def cart_detail(request):
    return HttpResponse("سبد خرید شما - تست")


def remove_from_cart(request, product_id):
    return HttpResponse(f'حذف محصول {product_id} از سبد خرید - تست')
