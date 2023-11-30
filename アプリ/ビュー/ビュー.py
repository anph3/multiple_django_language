from rest_framework.viewsets import ViewSet as セットを表示します
from django.http import JsonResponse as _json応答
from rest_framework.response import Response as 応答

# ここでビューを作成します.
class ベースビュー(セットを表示します):
    def __init__(自己, *引数, **キーワード引数):
        super().__init__(*引数, **キーワード引数)
    
    def データ応答(自己, データ=None, 状態=1, メッセージ="成功"):
        return {
            'ステータスコード': 状態,
            'メッセージ': メッセージ,
            'データ': データ
        }
        
    def 応答_データ(自己, データ=None, 状態=1, メッセージ="成功"):
        return 応答(自己.データ応答(データ, 状態, メッセージ))
    
    def json応答(自己, データ=None, 状態=1, メッセージ="成功"):
        return _json応答(自己.データ応答(データ, 状態, メッセージ))