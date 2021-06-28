from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from .models import Watchlist, StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer


class StreamPlatformAV(APIView):
	def get(self, request):
		platform = StreamPlatform.objects.all()
		serializer = StreamPlatformSerializer(platform, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = StreamPlatformSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class WatchListAV(APIView):
	def get(self, request):
		watchlist = Watchlist.objects.all()
		serializer = WatchListSerializer(watchlist, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = WatchListSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class WatchDetailAV(APIView):
	def get(self, request, pk):
		try:
			movie = Watchlist.objects.get(pk=pk)
		except Watchlist.DoesNotExist:
			return Response({'error': 'Movie Not found'}, status=HTTP_404_NOT_FOUND)
		serializer = WatchListSerializer(movie)
		return Response(serializer.data)

	def put(self, request, pk):
		movie = Watchlist.objects.get(pk=pk)
		serializer = WatchListSerializer(movie, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		movie = Watchlist.objects.get(pk=pk)
		movie.delete()
		return Response(status=HTTP_204_NO_CONTENT)
