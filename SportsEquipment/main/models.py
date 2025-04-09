from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,PermissionsMixin
# Create your models here.


class REQUESTAPPROVE(models.TextChoices):
    PENDING = 'pending', 'Pending'
    APPROVE = 'approve', 'Approve'
    DENIED = 'denied', 'Denied'
  


class StudentBorrow(models.Model):
    id =models.AutoField(primary_key=True)
    student_no = models.IntegerField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    code_request = models.CharField(max_length=20, blank=True, null=True)
    request_status = models.CharField(max_length=50, choices=REQUESTAPPROVE.choices, default=REQUESTAPPROVE.PENDING)
    def __str__(self):
        return f"{self.code_request}"  
    
    
class ItemRequest(models.Model):
    id = models.AutoField(primary_key=True)
    equipment_name = models.CharField(max_length=255)
    quantity = models.IntegerField(blank=True, null=True)
    id_student_borrow = models.ForeignKey(StudentBorrow, on_delete=models.CASCADE)

    

class UserSiteManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Hash password properly
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
     
        extra_fields.setdefault('is_staff', True)  # Ensure is_staff is True for superuser
        extra_fields.setdefault('is_superuser', True)  # Ensure is_superuser is True for superuser
        extra_fields.setdefault('is_active', True)  # Ensure is_active is True for superuser
        return self.create_user(username, password, **extra_fields)
    

class UserSites(AbstractBaseUser,PermissionsMixin,BaseUserManager):
    ID = models.AutoField(primary_key=True)
    email = models.CharField(max_length=255, blank=True, null= True)
    password = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)  # Indicates whether the user can log in
    is_staff = models.BooleanField(default=False)  # Determines if the user can access the admin site
    is_superuser = models.BooleanField(default=False)  # If True, the user has all permissions
    
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='user_sites',  # Custom related_name to avoid the clash
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='user_sites_permissions',  # Custom related_name to avoid clash
        blank=True
    )
    
    # Add these fields

   
    objects = UserSiteManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def save(self, *args, **kwargs):
        # Hash the password before saving (only if it's not already hashed)
        if not self.password.startswith('pbkdf2_sha256$'):
            #self.password = make_password(self.password)
            self.set_password(self.password) 
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.username}"  
    
