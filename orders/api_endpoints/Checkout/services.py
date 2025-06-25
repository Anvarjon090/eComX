from accounts.models import User
from orders.models import Order, OrderItem
from products.models import ProductVariant
from orders.choices import CheckoutSourceChoices
from common.choices import OrderStatus


def create_order(source: str, user: User, product: int = None, quantity: int = 1):
    if source == CheckoutSourceChoices.CART:
        order = Order.objects.create(
            user=user, total_price=0, status=OrderStatus.PENDING
        )

        for item in user.cart.cart_items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price * item.quantity,
            )
            order.total_price += item.product.price * item.quantity

        order.save()

        for item in user.cart.cart_items.all():
            item.delete()

        return order

    elif source == CheckoutSourceChoices.PRODUCT:
        product_obj = ProductVariant.objects.filter(id=product).first()
        if not product_obj:
            return None

        order = Order.objects.create(
            user=user,
            total_price=product_obj.price * quantity,
            status=OrderStatus.PENDING,
        )
        OrderItem.objects.create(
            order=order,
            product=product_obj,
            quantity=quantity,
            price=product_obj.price * quantity,
        )
        return order

    return None
