from django.urls import path
from . import views

app_name = 'order'


urlpatterns = [
    path('<int:pk>/add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('<int:pk>/remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.view_cart, name='view_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
