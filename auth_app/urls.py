from django.urls import path
from auth_app import views

urlpatterns = [
    path('signup/', views.user_signup, name='authapp-signup'),
    path('login/', views.user_login, name='authapp-login'),
    path('logout/', views.user_logout, name='authapp-logout'),
]