from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin): # 우리는 UserAdmin에 대해서도 상속받기 때문에 이 안에 있는 코드도 가져와서 수정해야함.
    fieldsets = (
        (
            "Profile", 
            {
                "fields":(
                "avatar",
                "username",
                "password",
                "name",
                "email",
                "is_host",
                "gender",
                "language",
                "currency",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
         ),
        (
            "Important Dates", 
            {
                "fields": (
                    "last_login", 
                    "date_joined"
                ),
            },
        ),
    )

    list_display = ("username", "email", "name", "is_host") # admin 패널 화면에서 보여줄 컬럼 설정.