from cart.models import Cart, CartItem
from .models import Order, OrderItem

def create_order_from_cart(user, address):
    cart = user.cart
    if cart.items.count() == 0:
        return None

    order = Order.objects.create(
        user=user,
        address=address,
        total_amount=cart.total_price
    )

    for item in cart.items.all():
        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price_at_time=item.price_at_time
        )

    # خالی کردن سبد
    cart.items.all().delete()

    return order
