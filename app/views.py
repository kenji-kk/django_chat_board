from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from .forms import CustomUserCreationForm 
from django.contrib.auth.decorators import login_required


def signup(request):
  if request.method == 'POST':
    form = CustomUserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      input_email = form.cleaned_data['email']
      input_password = form.cleaned_data['password1']
      new_user = authenticate(
        email=input_email,
        password=input_password,
      )
      if new_user is not None:
        login(request, new_user)
        return redirect('app:userdetail')
  else:
    form = CustomUserCreationForm()
  return render(request, 'app/signup.html', {'form': form})

@login_required
def userdetail(request):
  user = request.user
  userclass = get_user_model()
  user_object = get_object_or_404(userclass , id=user.id)
  return render(request, 'app/userdetail.html', {'user_object': user_object})
