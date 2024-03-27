from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from item.models import Item
from order.models import Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

@login_required
def index(request):
    user_items = Item.objects.filter(created_by=request.user)
    orders = Order.objects.filter(user=request.user).prefetch_related('orderitem_set')  # Prefetch related items for performance
    status = request.user.status

    return render(request, 'dashboard/index.html', {
        'user_items': user_items,
        'status': status,
        'orders': orders,
    })


@login_required
@require_POST
def return_item(request, pk):
    order_item = get_object_or_404(OrderItem, id=pk, order__user=request.user)
    order_item.delete()
    messages.success(request, "Item returned successfully.")
    return redirect('dashboard:index')
