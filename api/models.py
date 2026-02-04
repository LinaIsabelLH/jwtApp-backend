from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Vous devez avoir un email")
        if not password:
            raise ValueError("Vous devez fournir un mot de passe")
        email= self.normalize_email(email)
        user= self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        return self.create_user(email, password, **extra_fields)


class CustomUser (AbstractUser):
    username=None 
    email = models.EmailField(unique=True)

    ACCOUNT_TIERS=(
        ("FREE", "Free"),
        ("PREMIUM", "Premium"),
        ("UNLIMITED", "Unlimited")
    )

    STATUS_CHOICES =(
        ("ACTIVE", "Active"),
        ("BLOCKED", "Blocked"),
        ("DELETED", "Deleted")
    )

    account_tier = models.CharField(max_length=20, choices=ACCOUNT_TIERS, default="FREE")
    status= models.CharField(max_length=20, choices=STATUS_CHOICES, default="ACTIVE")
    is_staff = models.BooleanField()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS =[]

    objects= CustomUserManager()

    def __str__(self):
        return self.email