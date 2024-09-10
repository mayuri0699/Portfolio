from django.urls import path,include
from apps.folioadmin.views import registretion
# from apps.folioadmin.views.registretion import Signin, Signup, Logout, ForgetPasswordView, ResetPasswordView, Index

urlpatterns = [
    path("", registretion.Signin.as_view(), name="sign_in"),
    path('signup', registretion.Signup.as_view(), name="sign_up"),
    path('index', registretion.Index.as_view(), name="index"),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('forget_password/', registretion.ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/', registretion.ResetPasswordView.as_view(), name='reset_password'),
    path('logout/', registretion.Logout.as_view(), name='logout'),   
    
]

