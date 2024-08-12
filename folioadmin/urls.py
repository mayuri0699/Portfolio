
from django.urls import path
from . import views

urlpatterns = [
   path('',views.adminlogin, name='adminlogin'),
   # path('adminregister',views.adminregister, name='adminregister'),
   path('logout',views.logout,name='logout'),
   path('index',views.index, name='index'),

   path('bannerpage',views.bannerpage,name='bannerpage'),
   path('bannerform',views.bannerform,name='bannerform'),
   path('banner_update/<int:id>',views.banner_update,name='banner_update'),
   path('banner_delete/<int:id>',views.banner_delete,name='banner_delete'),

   path('aboutpage',views.aboutpage,name='aboutpage'),
   path('aboutform',views.aboutform,name='aboutform'),
   path('about_update/<int:id>',views.about_update,name='about_update'),
   path('about_delete/<int:id>',views.about_delete,name='about_delete'),
   
   path('educationpage',views.educationpage,name='educationpage'),
   path('educationform',views.educationform,name='educationform'),
   path('education_update/<int:id>',views.education_update,name='education_update'),
   path('education_delete/<int:id>',views.education_delete,name='education_delete'),
   
   path('skillspage',views.skillspage,name='skillspage'),
   path('skillsform',views.skillsform,name='skillsform'),
   path('skills_update/<int:id>',views.skills_update,name='skills_update'),
   path('skills_delete/<int:id>',views.skills_delete,name='skills_delete'),

   path('projectpage',views.projectpage,name='projectpage'),
   path('projectform',views.projectform,name='projectform'),
   path('project_update/<int:id>',views.project_update,name='project_update'),
   path('project_delete/<int:id>',views.project_delete,name='project_delete'),

   path('servicepage',views.servicepage,name='servicepage'),
   path('serviceform',views.serviceform,name='serviceform'),
   path('service_update/<int:id>',views.service_update,name='service_update'),
   path('service_delete/<int:id>',views.service_delete,name='service_delete'),

   path('interestpage',views.interestpage,name='interestpage'),
   path('interestform',views.interestform,name='interestform'),
   path('interest_update/<int:id>',views.interest_update,name='interest_update'),
   path('interest_delete/<int:id>',views.interest_delete,name='interest_delete'),

   path('socialaccount',views.socialaccount,name='socialaccount'),
   path('socialaccountform',views.socialaccountform,name='socialaccountform'),
   path('socialaccount_update/<int:id>',views.socialaccount_update,name='socialaccount_update'),
   path('socialaccount_delete/<int:id>',views.socialaccount_delete,name='socialaccount_delete'),



   path('massagepage',views.massagepage,name='massagepage'),
   path('massage_delete/<int:id>',views.massage_delete,name='massage_delete'),

    
]
