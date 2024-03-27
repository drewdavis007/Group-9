from django.shortcuts import render, redirect
from item.models import Category, Item
from .forms import SignupForm

# Create your views here.

def index(request):
    items = Item.objects.filter(is_sold=False, is_approved=True)
    # Fetch parent categories
    parent_categories = Category.objects.filter(parent__isnull=True)
    
    # Prepare categories with item counts
    categories_with_counts = []
    for category in parent_categories:
        # Sum item counts in all subcategories
        item_count = Item.objects.filter(category__parent=category, is_sold=False, is_approved=True).count()
        categories_with_counts.append((category, item_count))
    
    return render(request, 'root/index.html', {
        'categories_with_counts': categories_with_counts,
        'items': items,
    })


def contact(request):
    return render(request, 'root/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid(): 
            form.save() 

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'root/signup.html', {
        'form': form
    })
