from . import ビュー
from ..モデル.モデル import ユーザー
from ..シリアライザ.ユーザーシリアライザー import ユーザーシリアライザー
from 一般.構成.翻訳する import *

class 認証ビュー(ビュー.ベースビュー):
    def こんにちは(ビュー, リクエスト):
        _データ = {"テスト": "こんにちは"}
        return ビュー.応答_データ(_データ)
    
    def すべてのユーザーを取得します(自己, リクエスト):
        ユーザークエリセット = ユーザー.オブジェクト.すべてのユーザーを取得します()
        シリアライザ = ユーザーシリアライザー(ユーザークエリセット, **{多くの:真実})
        結果 = 属性を取得する(シリアライザ, データ)
        return 自己.応答_データ(結果)
    
    def ログイン(自己, リクエスト):
        _データ = 属性を取得する(属性を取得する(リクエスト, データ),コピー)()
        return 自己.応答_データ(_データ)
        