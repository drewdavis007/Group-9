from django.test import TestCase
from django.contrib.auth import get_user_model
from item.models import Item, Category
from order.models import Order, OrderItem
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse


'''
test if the dashboard is accessible by authenticated users and correctly 
displays items or orders based on the user status.
'''

class DashboardViewTests(TestCase):
    def setUp(self):
        # Create a test user
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', email="test@testing.com", password='testpass123', status='seller')
        self.category = Category.objects.create(name="Electronics")
        self.item = Item.objects.create(
                    name="Laptop", 
                    description="A powerful machine.", 
                    price=1000.00, category=self.category, 
                    created_by=self.user, 
                    is_approved=True,
                    image=SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/jpeg'),
                    )        
        self.client.login(username='testuser', password='testpass123')

    def test_dashboard_access_by_authenticated_user(self):
        response = self.client.get(reverse('dashboard:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "My items")

    def test_dashboard_displays_items_for_buyer(self):
        # Assuming 'status' field exists on your user model and can be 'seller'
        self.user.status = 'seller'
        self.user.save()
        
        response = self.client.get(reverse('dashboard:index'))
        self.assertContains(response, self.item.name)

    '''
    test the "return item" functionality to ensure it correctly marks an item as returned.
    '''
    def test_return_item(self):
        self.buyer = get_user_model().objects.create_user(username='testbuyer', email="test@testing.com", password='testpass123', status='buyer')
        order = Order.objects.create(user=self.buyer, paid_amount=1000.00)
        order_item = OrderItem.objects.create(item=self.item, order=order, price=self.item.price, seller=self.user, quantity=1)

        response = self.client.post(reverse('dashboard:return_item', args=[order_item.id]))
        order_item.refresh_from_db()  # Refresh the instance to get updated fields from the database

        buyer_orders = Order.objects.filter(user=self.buyer).prefetch_related('orderitem_set')
        self.assertTrue(order_item not in buyer_orders)
