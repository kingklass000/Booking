from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = PhoneNumberField(region='KG')
    STATUS_CHOICES = (
        ('владелец' , 'Владелец'),
        ('клиент' , 'Клиент')
    )
    status_user = models.CharField(choices=STATUS_CHOICES, max_length=12)
    date = models.DateTimeField()

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=34)
    description = models.TextField()
    country = models.CharField(max_length=22)
    city = models.CharField(max_length=22)
    address = models.CharField(max_length=32)



class HotelPhotos(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='hotel_images/')
    video = models.FileField(upload_to='hotel_videos/')



class Room(models.Model):
    room = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveSmallIntegerField(default=0)
    area = models.PositiveSmallIntegerField(default=0)
    price_per_night = models.PositiveSmallIntegerField(default=0)



class RoomPhotos(models.Model):
    hotel = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')
    video = models.FileField(upload_to='room_videos/')



class Review(models.Model):
    author = models.CharField(max_length=22)
    text = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='review')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')
    created_date = models.DateTimeField()




