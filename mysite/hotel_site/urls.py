from django.urls import path
from .views import *

urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', HotelListViewSet.as_view({'get':'list', 'post':'create'}), name= 'hotel_list'),
    path('<int:pk>/', HotelDetailViewSet.as_view({'get': 'retrieve', 'put':'update',
                                              'delete': 'destroy'}), name = 'hotel_detail'),

    path('users/', UserViewSet.as_view({'get':'list'}), name= 'user_list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve'}), name = 'user_detail'),

    path('photos/', HotelPhotosViewSet.as_view({'get':'list', 'post':'create'}), name= 'photos_list'),
    path('photos/<int:pk>/', HotelPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                         'delete': 'destroy'}), name='room_photos_detail'),

    path('rooms/', RoomViewSet.as_view({'get':'list', 'post':'create'}), name= 'room_list'),
    path('rooms/<int:pk>/', RoomViewSet.as_view({'get': 'retrieve', 'put':'update',
                                              'delete': 'destroy'}), name = 'room_detail'),
    path('room_photos/', RoomPhotosViewSet.as_view({'get':'list', 'post':'create'}), name= 'room_photos_list'),
    path('room_photos/<int:pk>/', RoomPhotosViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                             'delete':'destroy'}), name='room_photos_detail'),

    path('rating/', RatingViewSet.as_view({'get':'list', 'post':'create'}), name= 'rating_list'),
    path('rating/<int:pk>/', RatingViewSet.as_view({'get': 'retrieve', 'put':'update',
                                              'delete': 'destroy'}), name = 'rating_detail'),

    path('review/', ReviewViewSet.as_view({'get':'list', 'post':'create'}), name= 'review_list'),
    path('review/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                    'delete': 'destroy'}), name='review_detail'),

]