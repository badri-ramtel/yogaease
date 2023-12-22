from django.shortcuts import render, redirect

def home(request):
    return render(request,'myapp/home.html')

def courses(request):
    return render(request, 'myapp/courses.html')

def about_us(request):
    return render(request, 'myapp/about.html')

def prices(request):
    return render(request, 'myapp/pricing.html')

def resources(request):
    return render(request, 'myapp/resources.html')