from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('userdetail/', views.user_detail, name='userdetail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('createboard', views.create_board, name='createboard'),
    path('timeline/', views.timeline, name='timeline')
]
