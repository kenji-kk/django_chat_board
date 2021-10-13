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
