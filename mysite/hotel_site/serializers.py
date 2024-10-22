from .models import *
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'



class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['first_name', 'last_name']



class HotelPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPhotos
        fields = '__all__'



class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'



class RoomPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomPhotos
        fields = '__all__'



class RatingSerializer(serializers.ModelSerializer):
    user = UserListSerializer()
    class Meta:
        model = Rating
        fields = ['user', 'hotel', 'stars']



class ReviewSerializer(serializers.ModelSerializer):
    author = UserListSerializer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
         model = Review
         fields = ['author', 'text', 'hotel', 'created_date']



class HotelListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['hotel_name', 'country', 'city',  'average_rating']


    def get_average_rating(self, obj):
        return obj.get_average_rating()



class HotelDetailSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    owner =  UserListSerializer()
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['hotel_name', 'description', 'country', 'city', 'address',
                  'owner', 'reviews', 'ratings', 'average_rating', 'video']


    def get_average_rating(self, obj):
        return obj.get_average_rating()