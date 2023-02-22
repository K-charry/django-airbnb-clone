from django.db import models
from django.contrib.auth.models import AbstractUser # 장고가 기본적으로 가지고 있는 User를 가져오기 위함.

class User(AbstractUser): # AbstractUser 코드를 수정해줘야 함. (직접 들어가서 수정은 XX, 카피해서 가져오고 여기서 수정)
    
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male") # 첫번째 값은 데이터베이스 값, 두번째 값은 admin 패널에서 보여지는 이름(label)
        FEMALE = ("female", "Female") # 첫번째 값은 설정한 max_length 보다 길이가 작아야 함을 주의.
    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "english")
    # 파이썬에서 Tuple을 만들 때 꼭 ()가 있어야 하는건 아님.
    class CurrencyChoices(models.TextChoices):
        WON = "won", "korean Won"
        USD = "use", "Dollar"
    
    first_name = models.CharField(
        max_length=150, editable=False,
    )
    last_name = models.CharField(
        max_length=150, editable=False,
    )
    avatar = models.ImageField(
        blank=True # 사진 등록을 하지 않아도 됨. (필수사항 X)
    )
    name = models.CharField(
        max_length=150, default="",
    )
    is_host = models.BooleanField(
        default=False,
    )
    gender = models.CharField(
        max_length=10, 
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2, 
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )

