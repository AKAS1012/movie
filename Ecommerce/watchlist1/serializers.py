from rest_framework import serializers

from .models import Watchlist, StreamPlatform


class StreamPlatformSerializer(serializers.ModelSerializer):

	class Meta:
		model = StreamPlatform
		fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):

	class Meta:
		model = Watchlist
		fields = "__all__"
