from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Room(models.Model):
    name = models.CharField("ルーム名", max_length=50)
    status = models.PositiveSmallIntegerField("状態", choices=[
        (1, "作成"),
        (2, "参加"),
        (3, "満室"),
    ])
    is_play = models.BooleanField("プレイ中", default=False)
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.name

class Member(models.Model):
    room = models.OneToOneField(Room, verbose_name="ルーム", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __str__(self):

        return self.room


class Picture(models.Model):
    # Userが削除された場合pictureも削除される
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="作成者", on_delete=models.CASCADE)
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    img = models.ImageField("イメージ", upload_to="drawing/picture")

    class Meta:
        verbose_name = "Picture"
        verbose_name_plural = "Pictures"

    def __str__(self):
        return f'作成者:{self.created_by} / 作成日時: {self.created_at}'
