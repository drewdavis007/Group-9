from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertEqual(user.status, 'buyer', "Default status should be 'buyer'")

    def test_create_user_with_status_seller(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='selleruser',
            email='seller@example.com',
            password='testpass123',
            status='seller'
        )
        self.assertEqual(user.status, 'seller', "Status should be 'seller'")