"""
URL configuration for ocms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Frontend Views
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login_page'),
    path('register/', views.register_view, name='register_page'),
    path('dashboard/', views.dashboard_view, name='dashboard_page'),
    path('courses/', views.courses_view, name='courses_page'),
    path('course-detail/<int:id>/', views.course_detail_view, name='course_detail_page'),
    
    # API endpoints
    path('api/auth/', include('accounts.urls')),
    path('api/', include('courses.urls')),       # contains categories, courses, instructor/courses
    path('api/', include('enrollments.urls')),   # contains enroll, my-courses, course/<id>/progress
    path('api/', include('reviews.urls')),       # contains courses/<id>/reviews, reviews/my
    path('api/admin/', include('dashboard.urls')), # contains analytics, top-courses
]
