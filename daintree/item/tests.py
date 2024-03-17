from django.test import TestCase
from django.urls import reverse
from .models import Item, Category
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import NewItemForm


# Create your tests here.

class ItemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user
        cls.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass123',
            status='seller'
        )
        
        # Create a category
        cls.category = Category.objects.create(name='Test Category')
        
        # Create an item
        cls.item = Item.objects.create(
            category=cls.category,
            name='Test Item',
            description='Test Description',
            price=100.00,
            created_by=cls.user
        )

    def test_item_creation(self):
        self.assertEqual(self.item.name, 'Test Item')
        self.assertEqual(self.item.description, 'Test Description')
        self.assertEqual(self.item.price, 100.00)
        self.assertEqual(self.item.created_by, self.user)
        self.assertEqual(self.item.category, self.category)

    def test_category_str_method(self):
        self.assertEqual(str(self.category), 'Test Category')

    def test_item_str_method(self):
        self.assertEqual(str(self.item), 'Test Item')


class ItemListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create multiple items to test pagination or list display
        number_of_items = 5
        test_user = get_user_model().objects.create_user(username='testuser', email='test@example.com', password='testpass', status='seller')
        test_category = Category.objects.create(name='Electronics')

        # Create a test image
        test_image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')

        for item_id in range(number_of_items):
            Item.objects.create(
                name=f'Test Item {item_id}',
                description='A description here.',
                price=100.00 + item_id,
                category=test_category,
                created_by=test_user,
                image=test_image
            )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('item:items'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('item:items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'item/items.html')


class ItemFormTest(TestCase):

    def test_item_form_valid_data(self):
        test_category = Category.objects.create(name='Electronics')
        form_data = {
            'name': 'Test Item',
            'description': 'Some description here.',
            'price': 120.00,
            'category': test_category, 
            'created_by': 1,  # Assuming the user with ID 1 exists
            'image': SimpleUploadedFile('test_image.jpg', b'file_content', content_type='image/jpeg'),
        }
        form = NewItemForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_item_form_no_data(self):
        form = NewItemForm(data={})
        self.assertFalse(form.is_valid())
        self.assertGreater(len(form.errors), 0)  # Ensure there are errors
