from rest_framework.viewsets import ViewSet as 세트를_표시하십시오
from django.http import JsonResponse as _JSON_응답
from rest_framework.response import Response as 응답

# ここでビューを作成します.
class 기본보기(세트를_표시하십시오):
    def __init__(소유하다, *논쟁, **키워드_인수):
        super().__init__(*논쟁, **키워드_인수)
    
    def 데이터_응답(소유하다, 데이터=None, 상황=1, 메시지="성공"):
        return {
            '상태 코드': 상황,
            '메시지': 메시지,
            '데이터': 데이터
        }
        
    def 応答_데이터(소유하다, 데이터=None, 상황=1, 메시지="성공"):
        return 응답(소유하다.데이터_응답(데이터, 상황, 메시지))
    
    def JSON_응답(소유하다, 데이터=None, 상황=1, 메시지="성공"):
        return _JSON_응답(소유하다.데이터_응답(데이터, 상황, 메시지))