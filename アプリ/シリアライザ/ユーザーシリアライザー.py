from rest_framework.serializers import ModelSerializer as モデルシリアライザ
from ..モデル.モデル import ユーザー
class ユーザーシリアライザー(モデルシリアライザ):
    class Meta:
        model = ユーザー
        fields = '__al__'