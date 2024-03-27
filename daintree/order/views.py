from django.shortcuts import redirect, render, get_object_or_404
from .models import Cart, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from item.models import Item

# Create your views here.
@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Item, pk=pk)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(item=item, cart=cart)
    
    if not created:
        # If the item already exists in the cart, increment the quantity
        cart_item.quantity = 1
        cart_item.save()
    
    return redirect('item:detail', pk=item.id)


@login_required
def update_item_quantity(request, pk):
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
        cart_item.quantity = quantity
        cart_item.save()
    return redirect('order:view_cart')


@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, pk=pk, cart__user=request.user)
    cart_item.delete()
    return redirect('order:view_cart')


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'order/cart.html', {'cart': cart})


@login_required
def checkout(request):
    if request.method == 'POST':
        cart, created = Cart.objects.get_or_create(user=request.user)
        order = Order.objects.create(user=request.user)
        total_price = 0
        for cart_item in cart.items.all():
            total_price += cart_item.item.price * cart_item.quantity
            OrderItem.objects.create(
                order=order,
                item=cart_item.item,
                seller=cart_item.item.created_by,
                quantity=cart_item.quantity,
                price=cart_item.item.price
            )
            cart_item.delete() # Delete the cart item after adding to order

        order.paid_amount = total_price
        order.save()

        #delete the cart if it's no longer needed
        cart.delete()

        return redirect('order:confirmation')

    return render(request,'order/checkout.html')


def confirmation(request):
     return render(request, 'order/confirmation.html')
