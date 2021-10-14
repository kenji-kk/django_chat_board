from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, get_user_model
from .forms import CustomUserCreationForm, FormChatContent
from .forms import ChatBoard as FormChatBoard
from django.contrib.auth.decorators import login_required
from .models import ChatBoard


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
def user_detail(request):
  user = request.user
  #この下の2行いらないかも,request.userに全部含まれるため
  userclass = get_user_model()
  user_object = get_object_or_404(userclass , id=user.id)
  chat_boards = user_object.chatboard_set.all
  return render(request, 'app/userdetail.html', {'user_object': user_object, 'chat_boards': chat_boards})

  
@login_required 
def create_board(request):
  if request.method == 'POST':
    form = FormChatBoard(request.POST)
    if form.is_valid():
      chat_board = form.save(commit=False)
      chat_board.user = request.user
      chat_board.save()
      return redirect('app:userdetail')
  else:
    form = FormChatBoard()
  return render(request, 'app/createboard.html', {'form': form})

def timeline(request):
  chat_boards = ChatBoard.objects.all()
  return render(request, 'app/timeline.html', {'chat_boards': chat_boards})


def chatcontent(request, pk):
  form = FormChatContent()
  chat_board = ChatBoard.objects.get(id = pk)
  chat_comments = chat_board.chatcontent_set.all()
  print(chat_comments)
  return render(request, 'app/chatcontent.html', {'chat_comments': chat_comments,'form': form, 'chat_board': chat_board})


def createcomment(request, board_id):
  if request.method == 'POST':
    user = request.user
    #この下の2行いらないかも,request.userに全部含まれるため
    userclass = get_user_model()
    user_object = get_object_or_404(userclass , id=user.id)
    chat_board = ChatBoard.objects.get(id = board_id)
    form = FormChatContent(request.POST)
    if form.is_valid():
      chat_comment = form.save(commit=False)
      chat_comment.user_name = user_object
      chat_comment.chat_board = chat_board
      chat_comment.save()
    return redirect('app:chatcontent', pk=board_id )

