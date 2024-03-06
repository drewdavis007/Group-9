from django.shortcuts import render
from item.models import Category, Item


# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.all
    return render(request, 'root/index.html', {
        'categories': categories,
        'items': items,
    })


def contact(request):
    return render(request, 'root/contact.html')
