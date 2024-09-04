from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from apps.userapp.basecontent import BaseContent
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(email=email)

class UserAuth(AbstractBaseUser,  PermissionsMixin):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=False)
    is_two_factor_auth_active = models.BooleanField(default=False)
    login_count = models.PositiveIntegerField(default=0)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    otp=models.IntegerField(null=True,blank=True)
    otp_expire_at=models.DateTimeField(null=True,blank=True)
    is_otp_expired=models.BooleanField(default=False)
    user_image=models.FileField(upload_to='user_image',blank=True,null=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    DisplayList = ['id','email','is_active','is_two_factor_auth_active','login_count','is_staff','is_admin']
    searchable_fields = ['id','email']
    # class Meta:
    #     db_table ='marketplaceapp_propertyresalepurchaselead'


class ProfileTable(BaseContent):
    user_auth = models.OneToOneField(to=UserAuth,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40,null=True,blank=True)
    last_name = models.CharField(max_length=40,null=True,blank=True)
    home_address = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_image = models.FileField(upload_to='profile_images',blank=True,null=True)
    nationality = models.CharField(max_length=40,null=True,blank=True)
    marital_status = models.CharField(max_length=40,null=True,blank=True)
    resume = models.FileField(null=True, blank=True)
    facebook=models.CharField(max_length=100,null=True, blank=True)
    instagram=models.CharField(max_length=100,null=True, blank=True)
    linkdin=models.CharField(max_length=100,null=True,blank=True) 
    github=models.CharField(max_length=100,null=True, blank=True)
    religion=models.CharField(max_length=40,null=True,blank=True)
    gender=models.CharField(max_length=40,null=True,blank=True)
    profile=models.CharField(max_length=200)    # website developer java or full stack developer
    i_agree_on_terms_and_conditions = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    DisplayList = ['id','user_auth','first_name','last_name','phone_number','date_of_birth','nationality','marital_status','religion','gender','i_agree_on_terms_and_conditions']
    searchable_fields = ['id','name']


class Education(BaseContent):
    user_auth = models.ForeignKey(to=UserAuth, on_delete=models.CASCADE)
    education = models.CharField(max_length=250)
    university = models.CharField(max_length=500, blank=True, null=True)
    year = models.CharField(max_length=15, blank=True, null=True)
    percentage = models.CharField(max_length=10, blank=True, null=True)

    DisplayList = ['id','user_auth','education','university','year','percentage']
    searchable_fields = ['id']

class Skill(BaseContent):
    user_auth = models.ForeignKey(to=UserAuth, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=100)
    # skill_per = models.PositiveSmallIntegerField(blank=True, null=True)

    DisplayList = ['id','user_auth','skill_name']
    searchable_fields = ['id']

class Experience(BaseContent):
    user_auth = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=250)
    job_title = models.CharField(max_length=500, blank=True, null=True)
    details = models.TextField(blank=True, null=True) 
    start_date = models.DateField(blank=True, null=True)  
    end_date = models.DateField(blank=True, null=True) 

    DisplayList = ['id','user_auth','company_name','job_title','start_date','end_date']
    searchable_fields = ['id','company_name']

class Projects(BaseContent):
    user_auth = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    project_pic = models.ImageField(upload_to='project_pics', blank=True, null=True)
    discription = models.TextField(blank=True, null=True)

    DisplayList = ['id','user_auth','project_name']
    searchable_fields = ['id','project_name']

class Interests(BaseContent):
    user_auth = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    interest_name = models.CharField(max_length=100)
    interest_pic = models.ImageField(upload_to='interest_pics', blank=True, null=True)

    DisplayList = ['id','user_auth','interest_name']
    searchable_fields = ['id','interest_name']

class Language(BaseContent):
    user_auth = models.ForeignKey(UserAuth, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=100)

    DisplayList = ['id','user_auth','language_name']
    searchable_fields = ['id','language_name']    

class AchievementAwards(BaseContent):
    user_auth = models.ForeignKey(to=UserAuth, on_delete=models.CASCADE)
    achievementawards_name = models.CharField(max_length=100)

    DisplayList = ['id','user_auth','achievementawards_name']
    searchable_fields = ['id','achievementawards_name']

class Activity(BaseContent):
    user_auth = models.ForeignKey(to=UserAuth, on_delete=models.CASCADE)
    activity_name = models.CharField(max_length=100)

    DisplayList = ['id','user_auth','activity_name']
    searchable_fields = ['id','activity_name']

class Contacts(BaseContent):
    user_auth = models.ForeignKey(to=UserAuth, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    subject = models.CharField(max_length=600, blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    DisplayList = ['id','user_auth','name','email']
    searchable_fields = ['id','email']
