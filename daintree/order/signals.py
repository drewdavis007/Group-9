from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import OrderItem  # Adjust import based on your project structure
from conversation.models import Conversation, ConversationMessage
from django.conf import settings

@receiver(post_save, sender=OrderItem)
def notify_seller_of_purchase(sender, instance, created, **kwargs):
    if created:  # Ensuring it's a new purchase
        seller = instance.seller
        buyer = instance.order.user
        item = instance.item

        # Check if there's an existing conversation between buyer and seller about this item
        conversation = Conversation.objects.filter(item=item, members=seller).filter(members=buyer).first()

        if not conversation:
            # Create a new conversation if none exists
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(seller, buyer)

        # Craft the notification message
        message_content = f"Congratulations {seller.username}, your item '{item.name}' has been purchased by {buyer.username}. \
                            \nYou now have ${item.price} added to your balance"

        # Create a new message in the conversation
        ConversationMessage.objects.create(
            conversation=conversation, 
            content=message_content, 
            created_by=buyer  # Assuming the buyer initiates this automated message
        )
