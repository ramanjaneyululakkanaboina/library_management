from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a user with an email instead of a username."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", True)  # Ensure user is active by default
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser with email instead of username."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class AdminUser(AbstractUser):
    email = models.EmailField(unique=True)
    username = None  # Remove the username requirement

    groups = models.ManyToManyField(Group, related_name="admin_users", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="admin_users_permissions", blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # No username, so no additional required fields

    objects = CustomUserManager()  # Use custom manager

    def __str__(self):
        return self.email


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
