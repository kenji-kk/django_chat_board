from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'app'
urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),

]
