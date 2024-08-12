from django.shortcuts import render,redirect
from folioadmin.models import*


# Create your views here.

def index(request):
    user = request.user
    try:
        userobj = User.objects.get(id = user.id)
    except User.DoesNotExist:
        userobj = None

    if BannerPage.objects.filter(user=userobj):
        bannerpageobj = BannerPage.objects.get(user=userobj)
    else:
        bannerpageobj = None

    if AboutPage.objects.filter(user=userobj):
        aboutpageobj = AboutPage.objects.get(user=userobj)
    else:
        aboutpageobj = None

    skillsobj = Skill.objects.filter(user=userobj)

    projectobj = Projects.objects.filter(user=userobj)

    servicesobj = Services.objects.filter(user=userobj)

    interestobj = Interests.objects.filter(user=userobj)

    if SocialAccount.objects.filter(user=userobj):
        socialaccountobj = SocialAccount.objects.get(user=userobj)
    else:
        socialaccountobj = None 

    educationtobj = Education.objects.filter(user=userobj)
    context={'bannerpageobj':bannerpageobj , 'aboutpageobj':aboutpageobj, 'skillsobj':skillsobj, 'projectobj':projectobj, 'servicesobj':servicesobj, 'interestobj':interestobj,'socialaccountobj':socialaccountobj,'educationtobj':educationtobj}
    return render(request, 'myfolio/index.html',context)



def massage(request):
    user=request.user
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        massage=request.POST.get('massage')
        print(name)
        print(email)
        print(subject)
        print(massage)
        # Contacts.objects.create(user=user,name=name,email=email,subject=subject,massage=massage)
        return redirect('/')
    
