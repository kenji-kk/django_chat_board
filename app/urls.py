from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('userdetail/', views.userdetail, name='userdetail'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('createboard',views.createboard, name='createboard')
]
