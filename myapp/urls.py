from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.home, name="myapp-home"),
    path('course/', views.courses, name="myapp-course"),
    path('about/', views.about_us, name="myapp-about"),
    path('pricing/', views.prices, name="myapp-pricing"),
    path('resource/', views.resources, name="myapp-resource")
]