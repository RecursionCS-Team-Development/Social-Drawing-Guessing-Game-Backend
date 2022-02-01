from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.

class Room(models.Model):
    name = models.CharField("ルーム名", max_length=50)
    password = models.CharField("パスワード", max_length=50, null=True, blank=True)
    entryNum = models.PositiveSmallIntegerField("参加人数", default=2, validators=[MinValueValidator(2), MaxValueValidator(6)])
    mode = models.CharField("ゲームモード", max_length=50, default="絵当てゲーム", choices=[
        ("絵当てゲーム", "絵当てゲーム"),
        ("伝言ゲーム", "伝言ゲーム"),
    ])
    level = models.CharField("レベル", max_length=50, default="medium", choices=[
        ("easy", "easy"),
        ("medium", "medium"),
        ("hard", "hard"),
    ])
    round = models.PositiveSmallIntegerField("ラウンド数", default=5, validators=[MinValueValidator(3), MaxValueValidator(7)])
    # status = models.PositiveSmallIntegerField("状態", default=1, choices=[
    #     (1, "作成"),
    #     (2, "参加"),
    #     (3, "満室"),
    # ])
    # is_play = models.BooleanField("プレイ中", default=False)
    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.name

class Member(models.Model):
    room = models.ForeignKey(Room, verbose_name="ルーム", on_delete=models.CASCADE)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name="メンバー", null=True, unique=True, on_delete=models.CASCADE)
    score = models.PositiveIntegerField("スコア", default=0, validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"

    def __str__(self):
        return f'{self.room.name}: {self.user}'


class ChatLog(models.Model):
    member = models.ForeignKey(Member, verbose_name="メンバー", on_delete=models.CASCADE)
    message = models.CharField("message", max_length=255)

    class Meta:
        verbose_name = "ChatLog"
        verbose_name_plural = "ChatLogs"

    def __str__(self):
        return f'{self.member}: {self.message}'


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
