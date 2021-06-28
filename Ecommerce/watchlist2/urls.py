from django.urls import path
from .views import StreamPlatformAV, WatchListAV, WatchDetailAV, StreamPlatformDetailAV, ReviewList, ReviewDetails


app_name = 'watchlist2'

urlpatterns = [
	path('list/', WatchListAV.as_view(), name='movie_list'),
	path('<int:pk>', WatchDetailAV.as_view(), name='movie_detail'),
	path('stream/', StreamPlatformAV.as_view(), name='stream_list'),
	path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream_detail'),
	path('stream/<int:pk>/review', ReviewList.as_view(), name='review_list'),
	path('stream/review/<int:pk>', ReviewDetails.as_view(), name='review_details'),

]
