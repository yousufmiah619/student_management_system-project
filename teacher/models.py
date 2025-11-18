from django.db import models
from authentications.models import UserProfile
from CustomAdmin.models import Course
class Teacher(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE,blank=True,null=True,related_name="teacher_profile")
    designation=models.CharField(max_length=200,blank=True,null=True)
    course=models.ForeignKey(Course,on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return self.user.first_name if self.user else "NO User"