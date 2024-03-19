from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Conversation, ConversationMessage
from item.models import Item, Category
from django.core.files.uploadedfile import SimpleUploadedFile

class ConversationModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user1 = get_user_model().objects.create_user(username='user1', email='user1@example.com', password='foo')
        cls.user2 = get_user_model().objects.create_user(username='user2', email='user2@example.com', password='bar')        
        cls.item = Item.objects.create(category = Category.objects.create(name='Test Category'),
                                       name='Test Item', 
                                       description='Test Description', 
                                       price=100.0, 
                                       created_by=cls.user1,
                                       image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
                                       )
        cls.conversation = Conversation.objects.create(item=cls.item)
        cls.conversation.members.add(cls.user1, cls.user2)

    def test_conversation_creation(self):
        self.assertEqual(self.conversation.item, self.item)
        self.assertTrue(self.conversation.members.filter(username='user1').exists())
        self.assertTrue(self.conversation.members.filter(username='user2').exists())


class ConversationMessageModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        cls.user = get_user_model().objects.create_user(username='user', email='user@example.com', password='foo')
        cls.other_user = get_user_model().objects.create_user(username='other_user', email='other_user@example.com', password='bar')
        cls.item = Item.objects.create(category = Category.objects.create(name='Test Category'),
                                       name='Test Item', 
                                       description='Test Description', 
                                       price=100.0, 
                                       created_by=cls.user,
                                       image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
                                       )
        cls.conversation = Conversation.objects.create(item=cls.item)
        cls.conversation.members.add(cls.user, cls.other_user)
        cls.message = ConversationMessage.objects.create(conversation=cls.conversation, content='Test Message', created_by=cls.user)

    def test_message_creation(self):
        self.assertEqual(self.message.conversation, self.conversation)
        self.assertEqual(self.message.content, 'Test Message')
        self.assertEqual(self.message.created_by, self.user)
