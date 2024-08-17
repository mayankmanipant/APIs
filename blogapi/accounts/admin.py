from django.contrib import admin # type: ignore
from django.contrib.auth.admin import UserAdmin # type: ignore

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=[
        "email",
        "username",
        "name",
        "is_staff",
    ]
    fieldsets=UserAdmin.fieldsets + ((None,{"fields":("name",)}), )
    add_fieldsets=UserAdmin.add_fieldsets + ((None,{"fields":("name",)}), )

admin.site.register(CustomUser, CustomUserAdmin)
