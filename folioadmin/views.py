from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.decorators import login_required



# Create your views here.

def adminlogin(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']

        user=authenticate(username=username,password=password)

        if user is not None:
            if user.is_superuser ==True and user.is_active == True and user.is_staff == True:
                login(request,user)
                return redirect('index')
            else:
                return redirect('/')
        else:
            return redirect('/')
    
    return render(request, 'folioadmin/login.html')



def logout(request):
    user = request.user
    auth.logout(request)
    return redirect('adminlogin')



@login_required
def index(request):
    return render(request, 'folioadmin/index.html')



def bannerpage(request):
    user = request.user
    userobj = User.objects.get(id = user.id)
    if BannerPage.objects.filter(user=userobj):
        bannerpageobj = BannerPage.objects.get(user=userobj)
    else:
        bannerpageobj = None
    
    return render(request,'folioadmin/banner_page.html', {'bannerpageobj':bannerpageobj})



def bannerform(request):
    user = request.user
    if request.method == 'POST':
        name=request.POST.get('name')
        profile=request.POST.get('profile')
        profilepic=request.FILES.get('profilepic')
        resume=request.FILES.get('resume')
        BannerPage.objects.create(user=user,name=name,profile=profile,profilepic=profilepic,resume=resume)
        return redirect('bannerpage')


def banner_update(request,id):
    bannerpageobj=BannerPage.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        profile=request.POST.get('profile')
        profilepic=request.FILES.get('profilepic')
        resume=request.FILES.get('resume')

        if profilepic:
            bannerpageobj.profilepic=profilepic
        if name:
            bannerpageobj.name=name
        if profile:
            bannerpageobj.profile=profile
        if resume:
            bannerpageobj.resume=resume

        bannerpageobj.save()
        return redirect('bannerpage')
    
    return render(request,'folioadmin/banner_update.html',{'bannerpageobj':bannerpageobj})

def banner_delete(request,id):
    data=BannerPage.objects.get(id=id)
    data.delete()
    return redirect('bannerpage')


def aboutpage(request):
    user = request.user
    userobj = User.objects.get(id = user.id)
    if AboutPage.objects.filter(user=userobj):
        aboutpageobj = AboutPage.objects.get(user=userobj)
    else:
        aboutpageobj = None
    return render(request,'folioadmin/about_page.html',{'aboutpageobj':aboutpageobj})


def aboutform(request):
    user = request.user
    if request.method == 'POST':
        email=request.POST.get('email')
        degree=request.POST.get('degree')
        phone_no=request.POST.get('phone_no')
        age=request.POST.get('age')
        about=request.POST.get('about')
        address=request.POST.get('address')
        profilepic1=request.FILES.get('profilepic1')
        years_exp=request.POST.get('years_exp')

        AboutPage.objects.create(user=user,email=email,degree=degree,phone_no=phone_no,age=age,about=about,address=address,profilepic1=profilepic1,years_exp=years_exp)
        return redirect('aboutpage')
    

def about_delete(request,id):
    data=AboutPage.objects.get(id=id)
    data.delete()
    return redirect('aboutpage')

def about_update(request,id):
    aboutpageobj=AboutPage.objects.get(id=id)
    user=request.user
    if request.method == 'POST':
        email=request.POST.get('email')
        degree=request.POST.get('degree')
        phone_no=request.POST.get('phone_no')
        age=request.POST.get('age')
        about=request.POST.get('about')
        address=request.POST.get('address')
        profilepic1=request.FILES.get('profilepic1')
        years_exp=request.POST.get('years_exp')

        if profilepic1:
            aboutpageobj.profilepic1=profilepic1
        if email:
            aboutpageobj.email=email
        if degree:
            aboutpageobj.degree=degree
        if phone_no:
            aboutpageobj.phone_no=phone_no
        if age:
            aboutpageobj.age=age
        if about:
            aboutpageobj.about=about
        if address:
            aboutpageobj.address=address
        if years_exp:
            aboutpageobj.years_exp=years_exp
        
        aboutpageobj.save()
        return redirect('aboutpage')

    return render(request,'folioadmin/about_update.html',{'aboutpageobj':aboutpageobj})  
    
def educationpage(request):
    user = request.user
    userobj = User.objects.get(id=user.id)
    educationobj = Education.objects.filter(user=userobj)
    return render(request,'folioadmin/education_page.html',{'educationobj':educationobj})

def educationform(request):
    user=request.user
    if request.method == 'POST':
        education=request.POST.get('education')
        university=request.POST.get('university')
        year=request.POST.get('year')
        percentage=request.POST.get('percentage')   
        Education.objects.create(user=user,education=education,university=university,year=year,percentage=percentage)
        return redirect('educationpage')
    


def education_update(request,id):
    educationobj= Education.objects.get(id=id)
    if request.method == 'POST':
        education=request.POST.get('education')
        university=request.POST.get('university')
        year=request.POST.get('year')
        percentage=request.POST.get('percentage')

        if education :
            educationobj.education=education
        if university :
            educationobj.university=university
        if year :
            educationobj.year=year
        if percentage :
            educationobj.percentage=percentage

        educationobj.save()
        return redirect('educationpage')

    return render(request,'folioadmin/education_update.html',{'educationobj':educationobj})


def education_delete(request,id):
    data=Education.objects.get(id=id)
    data.delete()
    return redirect('educationpage')


def skillspage(request):
    user = request.user
    userobj = User.objects.get(id=user.id)
    skillobj = Skill.objects.filter(user=userobj)
    return render(request,'folioadmin/skills_page.html',{'skillobj':skillobj})

def skillsform(request):
    user=request.user
    if request.method == 'POST':
        skill_name= request.POST.get('skill_name')
        skill_per= request.POST.get('skill_per')
        Skill.objects.create(user=user,skill_name=skill_name,skill_per=skill_per)
        return redirect('skillspage')
    
def skills_update(request,id):
    skillobj= Skill.objects.get(id=id)
    if request.method == 'POST':
        skill_name= request.POST.get('skill_name')
        skill_per= request.POST.get('skill_per')

        if skill_name:
            skillobj.skill_name=skill_name
        if skill_per:
            skillobj.skill_per=skill_per

        skillobj.save()
        return redirect('skillspage')

    return render(request,'folioadmin/skills_update.html',{'skillobj':skillobj})

def skills_delete(request,id):
    data=Skill.objects.get(id=id)
    data.delete()
    return redirect('skillspage')


def projectpage(request):
    user = request.user
    userobj = User.objects.get(id=user.id)
    projectobj = Projects.objects.filter(user=userobj)
    return render(request,'folioadmin/project_page.html',{'projectobj':projectobj})

def projectform(request):
    user=request.user
    if request.method == 'POST':
        project_name= request.POST.get('project_name')
        project_pic= request.FILES.get('project_pic')
        Projects.objects.create(user=user,project_name=project_name,project_pic=project_pic)
        return redirect('projectpage')
    
def project_update(request,id):
    projectobj= Projects.objects.get(id=id)
    if request.method == 'POST':
        project_name= request.POST.get('project_name')
        project_pic= request.FILES.get('project_pic')
        print(project_name)
        print(project_pic)

        if project_pic:
            projectobj.project_pic=project_pic
        if project_name:
            projectobj.project_name=project_name

        projectobj.save()
        return redirect('projectpage')

    return render(request,'folioadmin/project_update.html',{'projectobj':projectobj})

def project_delete(request,id):
    data=Projects.objects.get(id=id)
    data.delete()
    return redirect('projectpage')

def servicepage(request):
    user = request.user
    userobj = User.objects.get(id=user.id)
    servicesobj = Services.objects.filter(user=userobj)
    return render(request,'folioadmin/service_page.html',{'servicesobj':servicesobj})

def serviceform(request):
    user=request.user
    if request.method == 'POST':
        service_name= request.POST.get('service_name')
        about_service= request.POST.get('about_service')
        service_pic= request.FILES.get('service_pic')
        Services.objects.create(user=user,service_name=service_name, about_service=about_service, service_pic=service_pic)
        return redirect('servicepage')
    
def service_update(request,id):
    servicesobj= Services.objects.get(id=id)
    if request.method == 'POST':
        service_name= request.POST.get('service_name')
        about_service= request.POST.get('about_service')
        service_pic= request.FILES.get('service_pic')

        if service_pic:
            servicesobj.service_pic=service_pic
        if service_name:
            servicesobj.service_name=service_name
        if about_service:
            servicesobj.about_service=about_service

        servicesobj.save()
        return redirect('servicepage')

    return render(request,'folioadmin/service_update.html',{'servicesobj':servicesobj})


def service_delete(request,id):
    data=Services.objects.get(id=id)
    data.delete()
    return redirect('servicepage')

def interestpage(request):
    user = request.user
    userobj = User.objects.get(id=user.id)
    interestobj = Interests.objects.filter(user=userobj)
    return render(request,'folioadmin/interest_page.html',{'interestobj':interestobj})

def interestform(request):
    user=request.user
    if request.method == 'POST':
        interest_name= request.POST.get('interest_name')
        interest_pic= request.FILES.get('interest_pic')
        Interests.objects.create(user=user,interest_name=interest_name,interest_pic=interest_pic)
        return redirect('interestpage')


def interest_delete(request,id):
    data=Interests.objects.get(id=id)
    data.delete()
    return redirect('interestpage')


def interest_update(request,id):
    interestobj= Interests.objects.get(id=id)
    if request.method == 'POST':
        interest_name= request.POST.get('interest_name')
        interest_pic= request.FILES.get('interest_pic')
        if interest_pic:
            interestobj.interest_pic=interest_pic
        if interest_name:
            interestobj.interest_name=interest_name
            
        interestobj.save()
        return redirect('interestpage')

    return render(request,'folioadmin/interest_update.html',{'interestobj':interestobj})
    

def socialaccount(request):
    user = request.user
    userobj = User.objects.get(id = user.id)
    if SocialAccount.objects.filter(user=userobj):
        socialaccountobj = SocialAccount.objects.get(user=userobj)
    else:
        socialaccountobj = None    
    return render(request,'folioadmin/socialaccount_page.html', {'socialaccountobj':socialaccountobj})


def socialaccountform(request):
    user = request.user
    if request.method == 'POST':
        facebook=request.POST.get('facebook')
        instagram=request.POST.get('instagram')
        linkdin=request.POST.get('linkdin')
        github=request.POST.get('github')
        SocialAccount.objects.create(user=user,facebook=facebook,instagram=instagram,linkdin=linkdin,github=github)
        return redirect('socialaccount')


def socialaccount_update(request,id):
    socialaccountobj=SocialAccount.objects.get(id=id)
    if request.method=='POST':
        facebook=request.POST.get('facebook')
        instagram=request.POST.get('instagram')
        linkdin=request.POST.get('linkdin')
        github=request.POST.get('github')
        
        if facebook:
            socialaccountobj.facebook=facebook
        if instagram:
            socialaccountobj.instagram=instagram
        if linkdin:
            socialaccountobj.linkdin=linkdin
        if github:
            socialaccountobj.github=github
    
        socialaccountobj.save()
        return redirect('socialaccount')
    
    return render(request,'folioadmin/socialaccount_update.html',{'socialaccountobj':socialaccountobj})

def socialaccount_delete(request,id):
    data=SocialAccount.objects.get(id=id)
    data.delete()
    return redirect('socialaccount')



def massagepage(request):
    user = request.user
    userobj = User.objects.get(id=user.id)
    contactobj = Contacts.objects.filter(user=userobj)
    return render(request,'folioadmin/contact_page.html', {'contactobj':contactobj})




def massage_delete(request,id):
    data=Contacts.objects.get(id=id)
    data.delete()
    return redirect('massagepage')




