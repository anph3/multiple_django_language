from django.db import models
from ..マネージャー.ユーザーマネージャー import ユーザーマネージャー

# ここでモデルを作成します。
class ユーザー(models.Model):
    class Meta:
        db_table = 'ユーザー'
    id = models.BigAutoField(primary_key=True)
    ユーザー名 = models.CharField(max_length=255)
    Eメール = models.CharField(max_length=255)
    パスワード = models.CharField(max_length=255)
    で作成されました = models.DateTimeField(auto_now_add=True)
    で更新されました = models.DateTimeField(auto_now=True)
    で削除されました = models.DateTimeField()
    オブジェクト = ユーザーマネージャー()