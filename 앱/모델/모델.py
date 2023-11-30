from django.db import models
from ..매니저.사용자_관리자 import 사용자_관리자

# 여기에 모델을 만듭니다.
class 사용자(models.Model):
    class Meta:
        db_table = '사용자'
    id = models.BigAutoField(primary_key=True)
    사용자_이름 = models.CharField(max_length=255)
    이메일 = models.CharField(max_length=255)
    비밀번호 = models.CharField(max_length=255)
    만들어졌습니다 = models.DateTimeField(auto_now_add=True)
    업데이트 = models.DateTimeField(auto_now=True)
    삭제 = models.DateTimeField()
    물체 = 사용자_관리자()