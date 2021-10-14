from django.db import models
from django.contrib.auth import get_user_model

class ChatBoard(models.Model):

  board_title = models.CharField(max_length=100)
  user = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
  )
  created_at = models.DateTimeField('登録日時', auto_now_add=True)

  def __str__(self):
    return self.title


class ChatContent(models.Model):

  user_name = models.ForeignKey(
    get_user_model(),
    on_delete=models.CASCADE
  )
  comment =  models.CharField(max_length=200)
  created_at = models.DateTimeField('コメント日', auto_now_add=True)
  chat_board = models.ForeignKey(
    ChatBoard,
    on_delete=models.CASCADE
  )
