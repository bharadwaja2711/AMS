from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('index/', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('output1/', views.output1, name="output1"),
    path('creditcard/', views.creditcard, name='creditcard'),
    path('debitcard/', views.debitcard, name='debitcard'),
    path('buy/', views.buy, name="buy"),
    path('sell/', views.sell, name="sell"),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
]
