from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BannerPage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    name=models.CharField(max_length=200)
    profile=models.CharField(max_length=200)
    profilepic=models.ImageField(upload_to='profile pic',blank=True,null=True)
    resume = models.FileField(null=True, blank=True)


class AboutPage(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    email=models.EmailField()
    degree = models.CharField(max_length=50)
    phone_no=models.CharField(max_length=13)
    age = models.PositiveSmallIntegerField(null=True)
    about=models.TextField()
    profilepic1=models.ImageField(upload_to='profile',null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    years_exp=models.CharField(max_length=15,null=True, blank=True)


class SocialAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)
    facebook=models.TextField(null=True, blank=True)
    instagram=models.TextField(null=True, blank=True)
    linkdin=models.TextField(null=True,blank=True) 
    github=models.TextField(null=True, blank=True)
    


class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    education=models.CharField(max_length=250)
    university=models.CharField(max_length=500, default=True ,blank=True,null=True)
    year=models.CharField(max_length=15,default=True ,blank=True,null=True)
    percentage=models.CharField(max_length=10, default=True ,blank=True,null=True)     
    
class Skill(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    skill_name=models.CharField(max_length=100)
    skill_per=models.IntegerField(default=True ,blank=True,null=True)

class Services(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    service_name=models.CharField(max_length=100)
    about_service=models.TextField()
    service_pic=models.ImageField(upload_to='service Picture',null=True,blank=True)

class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    project_name=models.CharField(max_length=100)
    project_pic=models.ImageField(upload_to='project pic',null=True,blank=True)


class Interests(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    interest_name=models.CharField(max_length=100)
    interest_pic=models.ImageField(upload_to='interest pic',null=True,blank=True)

class Contacts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=255, default=True,null=True, blank=True)
    email =models.EmailField()
    subject = models.CharField(max_length=600,default=True,null=True, blank=True)
    massage = models.TextField(default=True,null=True, blank=True)