from django import template
register = template.Library()

@register.filter
def cart_total(cart_items):
    """Sum up the total cost of items in the cart."""
    return sum(it.item.price * it.quantity for it in cart_items)
