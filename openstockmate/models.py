from django.db import models
import re
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from time import timezone

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, age=None, city=None, occupation=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, age=age, city=city, occupation=occupation, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        if user.last_password_change and (timezone.now() - user.last_password_change).days < 180:
            raise ValueError('You must change your password at least every 180 days.')
        if password:
            if not re.match(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$', password):
                raise ValueError('Password must contain at least one digit, one lowercase and one uppercase letter, and be at least 8 characters long.')
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)  
    verification_code = models.CharField(max_length=6, blank=True, null=True)
    reset_password_code = models.CharField(max_length=20, blank=True, null=True)
    objects = CustomUserManager()
    age = models.PositiveIntegerField(null=False)
    city = models.CharField(max_length=100, null=False)
    occupation = models.CharField(max_length=100, null=True, blank=True)  # Meslek, opsiyonel
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def verify_email(self):
        self.is_verified = True
        self.save()

    def send_verification_code(self):
        code = get_random_string(length=6, allowed_chars='0123456789')
        self.verification_code = code
        self.save()

        subject = 'Account Verification Code'
        message = f'Your verification code is: {code}'
        from_email = 'noreply@openstockmate.org'
        to_email = [self.email]

        send_mail(subject, message, from_email, to_email)
        

    def set_reset_password_code(self):
        code = get_random_string(length=20)
        self.reset_password_code = code
        self.save()

    def clear_reset_password_code(self):
        self.reset_password_code = None
        self.save()

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='customuser_set',  # Add a related_name
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='customuser_set',  # Add a related_name
    )
#indexebağla    


#buadaaaaaaaaaaaaaaaaaaaaaaaaa
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    parent_id = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)
    
class ComponentDocumentLink(models.Model):
    document = models.ForeignKey('Document', on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
#asılbağlantı 
class Component(models.Model):
    model = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True, null=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    package = models.ForeignKey('Package', on_delete=models.CASCADE)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    stock = models.IntegerField(default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    
    def get_user_components(user):
        return Component.objects.filter(user=user)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.model)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('component_detail', args=[str(self.slug)])
    
    
class DocumentType(models.Model):
    name = models.CharField(max_length=100)

class Document(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=500, blank=True, null=True)
    document_type = models.ForeignKey('DocumentType', on_delete=models.CASCADE)
    document_path = models.CharField(max_length=500)

class LocationType(models.Model):
    name = models.CharField(max_length=100)

class Location(models.Model):
    name = models.CharField(max_length=100)
    location_type = models.ForeignKey('LocationType', on_delete=models.CASCADE)
    parent_id = models.ForeignKey('Location', on_delete=models.CASCADE, blank=True, null=True)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)

class Package(models.Model):
    name = models.CharField(max_length=100)

class PurchaseDetail(models.Model):
    purchase = models.ForeignKey('Purchase', on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

class Purchase(models.Model):
    date = models.DateField()
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)

class Supplier(models.Model):
    name = models.CharField(max_length=100, unique=True)

class StockMovement(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    source_location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='source_location')
    destination_location = models.ForeignKey('Location', on_delete=models.CASCADE, related_name='destination_location')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
#kontrol et buruyarı ok mi?
class StockAlert(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    threshold = models.IntegerField()

    class Meta:
        unique_together = ('user', 'component')

    def __str__(self):
        return f"{self.user.username}'s Alert for {self.component.name}"

    def send_alert_email(self):
        subject = 'Stock Alert'
        message = f"The stock for {self.component.name} is below the threshold ({self.threshold})."
        from_email = 'noreply@openstockmate.org'  #güncelle
        to_email = [self.user.email]
        send_alert_email = send_mail#sorunvar 
        send_mail(subject, message, from_email, to_email)

class Feedback(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Feedback"        

class Log(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log - {self.created_at}"
