# Generated by Django 5.0.11 on 2025-02-15 18:39

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('role', models.CharField(choices=[('guest', 'Guest'), ('player', 'Player'), ('developer', 'Developer'), ('designer', 'Graphic Designer'), ('admin', 'System Admin')], default='guest', max_length=20)),
                ('is_verified', models.BooleanField(default=False)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Nam', 'Nam'), ('Nữ', 'Nữ')], max_length=3, null=True)),
                ('img', models.ImageField(blank=True, default='media/avt/default.jpg', upload_to='media/avt/')),
                ('groups', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='%(app_label)s_%(class)s_permissions', to='auth.permission')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DesignerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_info', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='designer_profile_dash', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_keys', models.JSONField(default=dict)),
                ('payment_info', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='games/')),
                ('leaderboard', models.JSONField(default=list)),
                ('reward_enabled', models.BooleanField(default=False)),
                ('points_conversion_rate', models.FloatField(default=1.0)),
                ('in_game_currency', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('total_plays', models.IntegerField(default=0)),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.developerprofile')),
            ],
        ),
        migrations.AddField(
            model_name='developerprofile',
            name='uploaded_games',
            field=models.ManyToManyField(blank=True, to='player.game'),
        ),
        migrations.CreateModel(
            name='GameAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('file', models.FileField(upload_to='assets/')),
                ('is_free', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('downloads', models.IntegerField(default=0)),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.designerprofile')),
            ],
        ),
        migrations.AddField(
            model_name='designerprofile',
            name='uploaded_assets',
            field=models.ManyToManyField(blank=True, to='player.gameasset'),
        ),
        migrations.CreateModel(
            name='GameReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='player.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('transaction_type', models.CharField(choices=[('deposit', 'Deposit'), ('withdrawal', 'Withdrawal'), ('purchase', 'Purchase')], default='deposit', max_length=20)),
                ('reference_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('asset', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.gameasset')),
                ('game', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='player.game')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
                ('rewards', models.JSONField(default=list)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerScore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-score'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SystemAdminProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manages_users', models.BooleanField(default=True)),
                ('manages_payments', models.BooleanField(default=True)),
                ('manages_content', models.BooleanField(default=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
