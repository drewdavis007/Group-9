from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with both username and email fields."""

    use_in_migrations = True

    def _create_user(self, username, email, password, status, **extra_fields):
        """Create and save a User with the given username, email, password, and status."""
        if not username:
            raise ValueError(_('The Username must be set'))
        if not email:
            raise ValueError(_('The Email must be set'))
        if not status:
            raise ValueError(_('The Status must be set'))
        
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, status=status, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, status='buyer', **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, status, **extra_fields)

    def create_superuser(self, username, email, password, status='seller', **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(username, email, password, status, **extra_fields)
