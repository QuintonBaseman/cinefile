from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('signup/', views.signupPage, name='signup'),
    path('login/', views.loginPage, name='login'),
    path('users/', views.userHomePage, name='users'),
    path('logout/', views.logoutUser, name='logout'),
    path('notallowed/', views.userHomePage, name='notallowed'),
    path('moviedetail/', views.movieDetail, name='moviedetail'),
]