from Auth import views
from django.urls import path

urlpatterns = [
    path('login/', views.Login, name = 'Login'),
    path('register/', views.Register, name = 'Register'),
    path('home/', views.Home, name = 'Home'),
    path('Logout',views.Logout, name = 'Logout'),
]
