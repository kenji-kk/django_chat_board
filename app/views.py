from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from .forms import CustomUserCreationForm, ChatBoard
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
        return redirect('app:user_detail')
  else:
    form = CustomUserCreationForm()
  return render(request, 'app/signup.html', {'form': form})


@login_required
def user_detail(request):
  user = request.user
  #この下の2行いらないかも,request.userに全部含まれるため
  userclass = get_user_model()
  user_object = get_object_or_404(userclass , id=user.id)
  chat_boards = user_object.chatboard_set.all
  return render(request, 'app/userdetail.html', {'user_object': user_object, 'chat_boards': chat_boards})

def create_board(request):
  if request.method == 'POST':
    form = ChatBoard(request.POST)
    if form.is_valid():
      chat_board = form.save(commit=False)
      chat_board.user = request.user
      chat_board.save()
      return redirect('app:userdetail')
  else:
    form = ChatBoard()
  return render(request, 'app/createboard.html', {'form': form})

