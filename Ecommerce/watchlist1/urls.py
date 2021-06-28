from django.urls import path

from .views import StreamPlatformAV, WatchListAV, WatchDetailAV

app_name = 'watchlist1'
urlpatterns = [
	path('list/', WatchListAV.as_view(), name='movie_list'),
	path('<int:pk>', WatchDetailAV.as_view(), name='movie_detail'),
	path('stream/', StreamPlatformAV.as_view(), name='stream_list'),

]
