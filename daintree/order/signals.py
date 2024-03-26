from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import OrderItem  # Adjust import based on your project structure
from conversation.models import Conversation, ConversationMessage

@receiver(post_save, sender=OrderItem)
def notify_seller_of_purchase(sender, instance, created, **kwargs):
    if created:  # Ensuring it's a new purchase
        seller = instance.seller
        buyer = instance.order.user
        item = instance.item
        quantity = instance.quantity

        conversation = Conversation.objects.create(item=item)
        conversation.members.add(seller, buyer)

        # Craft the notification message
        message_content = f"Congratulations {seller.username}, your item '{item.name}' has been purchased by {buyer.username}.\
                            \n{quantity} of the items were purchased. You now have ${quantity*item.price} added to your balance"

        # Create a new message in the conversation
        ConversationMessage.objects.create(
            conversation=conversation, 
            content=message_content, 
            created_by=buyer  # Assuming the buyer initiates this automated message
        )
