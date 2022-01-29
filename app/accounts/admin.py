from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()

class UserAdminCustom(UserAdmin):
    """
    管理画面の表示をカスタマイズする.
    ユーザーの詳細情報とユーザー一覧に表示される項目をオーバーライドする
    """
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'email',
                'password',
                'icon',
                'profile',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )

    #ユーザー追加時に入力する項目
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username',
                'email',
                'password1',
                'password2',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )

    # ユーザー一覧
    list_display = (
        'id',
        'username',
        'email',
        'is_active',
    )

    # 検索フィールド
    search_fields = (
        'username',
        'email',
    )

    # 並び順
    ordering = ('id',)



admin.site.register(User, UserAdminCustom)