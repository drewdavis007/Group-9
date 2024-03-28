
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Cart, CartItem, Order, OrderItem
from item.models import Item, Category
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse

class OrderModelsTestCase(TestCase):

    def setUp(self):
        # Create a test user
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )

        # Create a category
        cat = Category.objects.create(name='Test Category')
        
        # Create a test image
        test_image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        
        # Create an item
        self.item = Item.objects.create(
            category=cat,
            name='Test Item',
            description='Test Description',
            price=100.00,
            created_by=self.user,
            image=test_image
        )

    def test_cart_creation(self):
        # Test creating a cart for the user
        cart = Cart.objects.create(user=self.user)
        self.assertEqual(cart.user, self.user)

    def test_cartitem_creation(self):
        # Test adding an item to the cart
        cart = Cart.objects.create(user=self.user)
        cart_item = CartItem.objects.create(cart=cart, item=self.item, quantity=1)
        self.assertEqual(cart_item.cart, cart)
        self.assertEqual(cart_item.item, self.item)
        self.assertEqual(cart_item.quantity, 1)


class OrderViewsTestCase(TestCase):

    def setUp(self):
        # Create a test user and log them in
        User = get_user_model()
        self.user = User.objects.create_user(
            username='testuser2',
            email='test2@example.com',
            password='12345'
        )
        self.client.login(username='testuser2', password='12345')

        # Create a category
        cat = Category.objects.create(name='Test Category')
        
        # Create a test image
        test_image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        
        # Create an item
        self.item = Item.objects.create(
            category=cat,
            name='Test Item',
            description='Test Description',
            price=10.00,
            created_by=self.user,
            image=test_image
        )


    def test_add_to_cart_view(self):
        # Test adding an item to the cart through the view
        response = self.client.post(reverse('order:add_to_cart', kwargs={'pk': self.item.pk}))
        self.assertEqual(response.status_code, 302)  
        self.assertTrue(Cart.objects.exists())
        self.assertTrue(CartItem.objects.filter(item=self.item).exists())
