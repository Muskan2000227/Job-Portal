"""
URL configuration for Hire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myapp import views 

urlpatterns = [
    path("admin/", admin.site.urls),

    path("mainpage", views.mainpage, name="mainpage"),
    # Candidate
    path("signup_user", views.signup_user,name="signup_user"),
    path("login_user", views.login_user,name="login_user"),
    path("afterlogin", views.afterlogin,name="afterlogin"),
    path('logout_user',views.logout_user,name='logout_user'),

    # Employeer
    path("signup_emp", views.signup_emp,name="signup_emp"),
    path("login_emp", views.login_emp,name="login_emp"),
    path("afterlogine", views.afterlogine,name="afterlogine"),
    path('logout_emp',views.logout_emp,name='logout_emp'),

    path('',views.Home,name='Home'),
    path('search/', views.job_search, name='job_search'),
    path('companyprf', views.companyprf, name='companyprf'),
    path('editcompprf', views.editcompprf, name='editcompprf'),
    path('addjob',views.addjob,name='addjob'),
    path('jobshowcomp',views.jobshowcomp,name='jobshowcomp'),

    path('experienceuser',views.experienceuser,name='experienceuser'),
    path('educationuser',views.educationuser,name='educationuser'),
    path('skillsuser',views.skillsuser,name='skillsuser'),
    path('resume',views.resume,name='resume'),
    path('savedjobs',views.savedjobs,name='savedjobs'),
    path('appliedjobs',views.appliedjobs,name='appliedjobs'),
    path('jobsresshow/<int:job_id>/',views.jobresshow,name='jobresshow'),
    path('alljobs',views.alljobs,name="alljobs"),
    path('alljobsdetails/<int:job_id>/',views.alljobsdetails,name='alljobsdetails'),
    path('candidates',views.candidates,name='candidates'),
    path('resume',views.resume,name="resume"),
    path('resume2',views.resume2,name="resume2"),
    path('resume1',views.resume1,name="resume1"),
    path('resume3',views.resume3,name="resume3"),
    path('allresumes',views.allresumes,name="allresumes")
    
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
