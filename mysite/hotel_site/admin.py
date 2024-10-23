from django.contrib import admin
from .models import *


class HotelPhotosInline(admin.TabularInline):
    model = HotelPhotos
    extra = 1


class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelPhotosInline]


class RoomPhotosInline(admin.TabularInline):
    model = RoomPhotos
    extra = 1

class RoomAdmin(admin.ModelAdmin):
    inlines = [RoomPhotosInline]



admin.site.register(User)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Rating)
admin.site.register(Review)
