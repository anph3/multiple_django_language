from django.db.models import Manager as マネージャー
from 一般.構成.翻訳する import *

class ユーザーマネージャー(マネージャー):
    def すべてのユーザーを取得します(自己):
        return 属性を取得する(自己, 全て)()