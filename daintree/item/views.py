from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item
from django.shortcuts import get_object_or_404

  

def items(request):
    items = Item.objects.filter(is_sold=False) 

    return render(request, 'item/items.html',{
        'items':items,
    })


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html',{
        'item':item,
        'related_items': related_items
    })
