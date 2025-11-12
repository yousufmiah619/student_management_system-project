from django.db import models
from django.conf import settings
# Create your models here.
class AdminProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True,related_name="admin_profile")
    first_name=models.CharField(max_length=255,blank=True,null=True)
    last_name=models.CharField(max_length=255,blank=True,null=True)
    phone_number=models.CharField(max_length=20,blank=True,null=True)
    profil_picture=models.ImageField(upload_to="profil",blank=True,null=True)
    joined_date=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    def __str__(self):
        return self.user.email if self.user else "no User"
