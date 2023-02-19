from django.contrib import admin
from .models import House

@admin.register(House) # 이 Decorator는 'HouseAdmin' 클래스가 'House' 모델을 통제한다는 의미.
class HouseAdmin(admin.ModelAdmin):
    # Django에서는 list[]보다 tuple()이 자주 사용됨.
    list_display = ( # admin 패널내 House 모델의 column(=속성)을 화면에 띄우기 위한 방법.
        "name",
        "price_per_night",
        "address",
        "pets_allowed"
    )
    list_filter = ( # admin 패널내 House 모델의 column 필터링 기능.
        "price_per_night",
        "pets_allowed"
    )
    # 'address'라는 컬럼에 대해서만 검색하도록.(admin 패널내에서)
    # search_fields의 값은 list 거나 tuple 이여야만 함.
    search_fields = ("address",) # 한 개의 element를 가진 tuple을 사용한다면 뒤에 콤마를 붙여줘야함. 안그러면 그냥 string으로 인식 (VS Code에서)
    # ("address__startswith") # 검색할 단어로 시작하는 주소만 검색되도록. 그냥 "address"만 치면 포함되는 문자열이면 다 검색해서 나옴.
    # exclude = ("price_per_night",) # admin 페이지에서 해당 속성을 제외시키고 싶은 경우
    # field 는 form 형식을 바꿔줌. 
    fields = ( 
        "name",
        "address",
        ("price_per_night", "pets_allowed"),
    ) # "name","address"는 따로 "price_per_night"와 "pets_allowed"는 같은 컬럼내 위치한다.
    list_display_links = ("name", "address") # 이렇게하면 name 컬럼과 address 컬럼을 클릭만 해줘도 모델 내부로 들어갈 수 있다.
    list_editable = ("pets_allowed",) # 바로 보여지는 모델내 리스트내에서 해당 속성 편집하고 저장가능.

    
    
