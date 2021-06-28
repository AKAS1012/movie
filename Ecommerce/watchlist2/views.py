
from .serializers import WatchListSerializer, StreamPlatformSerializer, ReviewstSerialize
from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Watchlist, StreamPlatform, Reviews
from .permissions import AdminOrReadOnly, ReviewUserOrReadOnly

class ReviewDetails(mixins.RetrieveModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Reviews.objects.all()
	serializer_class = ReviewstSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)


class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Reviews.objects.all()
	serializer_class = ReviewstSerializer
	permission_classes = [AdminOrReadOnly]

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)


class StreamPlatformAV(APIView):
	def get(self, request):
		platform = StreamPlatform.objects.all()
		serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})
		return Response(serializer.data)

	def post(self, request):
		serializer = StreamPlatformSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors)


class StreamPlatformDetailAV(APIView):
	def get(self, request, pk):
		try:
			movie = StreamPlatform.objects.get(pk=pk)
		except StreamPlatform.DoesNotExist:
			return Response({'error': 'Movie Not found'}, status=HTTP_404_NOT_FOUND)
		serializer = StreamPlatformSerializer(movie)
		return Response(serializer.data)

	def put(self, request, pk):
		movie = StreamPlatform.objects.get(pk=pk)
		serializer = StreamPlatformSerializer(movie, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

	def delete(self, request, pk):
		movie = StreamPlatform.objects.get(pk=pk)
		movie.delete()
		return Response(status=HTTP_204_NO_CONTENT)


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
