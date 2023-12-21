from django.shortcuts import render, redirect

def home(request):
    return render(request,'myapp/home.html')

def courses(request):
    return render(request, 'myapp/courses.html')

def about_us(request):
    return render(request, 'myapp/about.html')