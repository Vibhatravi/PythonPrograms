from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/",views.SignupPage,name='signup'),
    path("",views.LoginPage,name='login'),
    path("logout/",views.logout,name='logout'),
    #path("main/",views.HomePage,name='main'),
    #path("main/", include("app1.urls")),
    #path("main/",views.HomePage,name='main'),
    path("main/", include("entries.urls"),name='main'),
]