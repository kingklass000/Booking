from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = PhoneNumberField(region='KG')
    STATUS_CHOICES = (
        ('владелец' , 'Владелец'),
        ('клиент' , 'Клиент'),
        ('администратор' , 'Администратор')
    )
    status_user = models.CharField(choices=STATUS_CHOICES, max_length=15)


    def __str__(self):
        return f'{self.first_name} - {self.last_name}'



class Hotel(models.Model):
    hotel_name = models.CharField(max_length=34)
    description = models.TextField()
    country = models.CharField(max_length=22)
    city = models.CharField(max_length=22)
    address = models.CharField(max_length=32)
    video = models.FileField(upload_to='hotel_videos/')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_name


    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0



class HotelPhotos(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name='hotel')
    image = models.ImageField(upload_to='hotel_images/', null=True, blank=True)



class Room(models.Model):
    room = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room_number = models.PositiveSmallIntegerField(default=0)
    area = models.PositiveSmallIntegerField(default=0)
    video = models.FileField(upload_to='room_videos/')
    price_per_night = models.PositiveSmallIntegerField(default=0)


    def __str__(self):
        return f'{self.room} - {self.room_number}'



class RoomPhotos(models.Model):
    hotel = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images/')



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='ratings')
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)], verbose_name='Рейтинг')

    def __str__(self):
        return f'{self.user}-{self.hotel}-{self.stars}stars'



class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='reviews')
    created_date = models.DateTimeField()

    def __str__(self):
        return f'{self.hotel} - {self.author}'





