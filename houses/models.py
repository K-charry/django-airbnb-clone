from django.db import models

class House(models.Model):
    """Model Definition for House"""
    name = models.CharField(max_length=140) 
    price_per_night = models.PositiveIntegerField(verbose_name="price", help_text="Positive Numbers Only")
    description = models.TextField() # TexrField는 CharField보다 훨씬 길게 쓸 수 있음.
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(
        verbose_name="Pets Allowed?",
        default=False, 
        help_text="Does this house allow pets?")
    
    def __str__(self): # House 클래스의 string method의 형태를 설정. (내 맘대로 프린트 느낌...)
        return self.name # 'House object (1)'이라는 이름 대신에 House class의 name이 보이도록.