from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from drawing.models import Member

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_firlds):
        if not email:
            raise ValueError('メールアドレスは必須です')

        email = self.normalize_email(email)
        email = email.lower()
        user = self.model(email=email, **extra_firlds)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password=None, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('メールアドレス', max_length=255, unique=True)
    username = models.CharField('名前', max_length=255)
    profile = models.TextField("自己紹介")
    icon = models.ImageField("アイコン", upload_to="users/icon", null=True)
    member = models.ForeignKey(Member, verbose_name="メンバー", on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    # メールアドレスとユーザー名が必須項目となる
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email