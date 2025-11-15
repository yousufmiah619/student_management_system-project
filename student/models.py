from django.db import models
from authentications.models import UserProfile
from CustomAdmin.models import Course
class Student(models.Model):
    user=models.OneToOneField(UserProfile,on_delete=models.CASCADE,blank=True,null=True,related_name="student_profile")
    roll_no=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.RESTRICT,blank=True,null=True)
    
    def __str__(self):
        return self.user.email if self.user else "NO User"