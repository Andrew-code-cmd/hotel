from django.db import models
from django.urls import reverse


class Room(models.Model):
    img = models.ImageField("Фото", upload_to="main_photos/", default=0)
    title = models.CharField("Вид номера", max_length=100)
    description = models.TextField("Описание")
    price = models.SmallIntegerField("Цена за сутки", default=0)
    price_2 = models.SmallIntegerField("Цена за сутки с завтраком", default=0)
    enable = models.SmallIntegerField("Сколько номеров данного типа свободно", default=0)
    url = models.SlugField(max_length=130, unique=True)

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    def __str__(self):
        return self.title

class RoomPhoto(models.Model):
    title = models.ImageField("Фото", upload_to="room_photos/")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'фото'
        verbose_name_plural = 'Фото номеров'