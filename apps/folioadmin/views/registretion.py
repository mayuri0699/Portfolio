from django.shortcuts import render, redirect , get_object_or_404
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from apps.userapp.models import *
# Create your views here.


class Signin(View):
    def get(self, request):
        return render(request,'template_folioadmin/auth-login.html')
    
    def post(self, request): # login count
        try:
            email = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(email = email, password = password)
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                messages.error(request,"Sorry, Incorrect Password. Please Try Again Or Reset Your Password If Needed.")
                return redirect("/")
        except:
            messages.error(request,"Something Went Wrong.")
            return redirect("/")
        
class Index(View):
    def get(self, request):
        return render(request, 'template_folioadmin/index.html')

class Signup(View):
    def get(self, request):
        return render(request, 'template_folioadmin/auth-register.html')
    
    def post(self, request):
        try:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            phone_number = request.POST.get('phone_number')
            email = request.POST.get("email").lower()
            password = request.POST.get("password")
            confirm_password = request.POST.get('confirm_password')
            i_agree_on_terms_and_conditions = request.POST.get('terms')

            if UserAuth.objects.filter(email=email).exists():
                messages.error(request, "User already exists with this email address")
                return redirect('sign_up')

            if password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect('sign_up')
            
            obj_user = UserAuth.objects.create_user(
                email=email, 
                password=password,
                is_active=True,
            )
            
            ProfileTable.objects.create(
                user_auth=obj_user,
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                i_agree_on_terms_and_conditions=bool(i_agree_on_terms_and_conditions)
            )
            
            return redirect("sign_in")  # Redirect to the sign-in page after successful signup
        except Exception as e:
            messages.error(request, f"Something went wrong: {str(e)}")
            return redirect('sign_up')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("/")
    
class ForgetPasswordView(View):
    def get(self, request):
        return render(request, 'template_folioadmin/auth-forget-pass.html')

    def post(self, request):
        email = request.POST.get('email').lower()
        if not email:
            messages.error(request, "Email is required")
            return redirect('forget_password')

        try:
            user = UserAuth.objects.get(email=email)
            # messages.success(request, "User found. You can reset your password now.")
            return redirect('reset_password')
        except UserAuth.DoesNotExist:
            messages.error(request, "User not found with the provided email")
            return redirect('forget_password')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('forget_password')
        
class ResetPasswordView(View):
    def get(self, request):
        return render(request, 'template_folioadmin/auth-reset-pass.html')

    def post(self, request):
        email = request.POST.get('email').lower()
        new_password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not email:
            messages.error(request, "Email is required")
            return redirect('reset_password')
        
        if new_password != confirm_password:
                messages.error(request, "Passwords do not match")
                return redirect('reset_password')

        try:
            user = UserAuth.objects.get(email=email)
            # Update user password
            user.set_password(new_password)
            user.save()
            messages.success(request, "Password reset Successfully")
            return redirect('sign_in')  # Redirect to login page after successful password reset
        except UserAuth.DoesNotExist:
            messages.error(request, "User not found with the provided email")
            return redirect('reset_password')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('reset_password')