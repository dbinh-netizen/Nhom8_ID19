from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Custom user model to handle different roles
class User(AbstractUser):
    ROLE_CHOICES = [
        ('guest', 'Guest'),
        ('player', 'Player'),
        ('developer', 'Developer'),
        ('designer', 'Graphic Designer'),
        ('admin', 'System Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='guest')
    is_verified = models.BooleanField(default=False)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # User account balance
    date_joined = models.DateTimeField(default=timezone.now)  # Track user registration date

# Player model for game interactions
class PlayerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    rewards = models.JSONField(default=list)  # Stores redeemed rewards
    last_active = models.DateTimeField(auto_now=True)  # Track last activity

# Developer model for game uploading
class DeveloperProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uploaded_games = models.ManyToManyField('Game', blank=True)
    api_keys = models.JSONField(default=dict)  # Stores API keys for leaderboard and payments
    payment_info = models.CharField(max_length=255, blank=True, null=True)

# Designer model for asset management
class DesignerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uploaded_assets = models.ManyToManyField('GameAsset', blank=True)
    payment_info = models.CharField(max_length=255, blank=True, null=True)

# Game model
class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    developer = models.ForeignKey(DeveloperProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='games/')
    leaderboard = models.JSONField(default=list)  # Stores player scores
    reward_enabled = models.BooleanField(default=False)
    points_conversion_rate = models.FloatField(default=1.0)  # Conversion rate for rewards
    in_game_currency = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)  # Status of the game
    total_plays = models.IntegerField(default=0)  # Track number of times played

# Game Asset model
class GameAsset(models.Model):
    title = models.CharField(max_length=255)
    designer = models.ForeignKey(DesignerProfile, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assets/')
    is_free = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)  # Status of the asset
    downloads = models.IntegerField(default=0)  # Track number of downloads

# System Admin model
class SystemAdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    manages_users = models.BooleanField(default=True)
    manages_payments = models.BooleanField(default=True)
    manages_content = models.BooleanField(default=True)  # Ability to manage games/assets

# Payment model for transactions
class PaymentTransaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending')
    transaction_type = models.CharField(max_length=20, choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal'), ('purchase', 'Purchase')], default='deposit')
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True)
    asset = models.ForeignKey(GameAsset, on_delete=models.SET_NULL, null=True, blank=True)
    reference_id = models.CharField(max_length=100, unique=True, null=True, blank=True)  # Track external payment reference
