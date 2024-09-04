from django.urls import path,include
from apps.folioadmin.views.registretion import Signin, Signup, Logout, ForgetPasswordView, ResetPasswordView

urlpatterns = [
    path("", Signin.as_view(), name="sign_in"),
    path('signup', Signup.as_view(), name="sign_up"),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('logout/', Logout.as_view(), name='logout'),   
    path('forget_password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/', ResetPasswordView.as_view(), name='reset_password'),
    
]

