from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import ChatBoard, ChatContent


class CustomUserCreationForm(UserCreationForm):
  class Meta:
    model = get_user_model()
    fields = ('email',)

class ChatBoard(ModelForm):
  class Meta:
    model = ChatBoard
    fields = ['board_title']

class FormChatContent(ModelForm):
  class Meta:
    model = ChatContent
    fields = ['comment']
