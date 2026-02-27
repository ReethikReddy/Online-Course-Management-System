from django.shortcuts import render

def home_view(request):
    return render(request, 'pages/home.html')

def login_view(request):
    return render(request, 'pages/login.html')

def register_view(request):
    return render(request, 'pages/register.html')

def dashboard_view(request):
    return render(request, 'pages/dashboard.html')

def courses_view(request):
    return render(request, 'pages/courses.html')

def course_detail_view(request, id):
    return render(request, 'pages/course_detail.html')
