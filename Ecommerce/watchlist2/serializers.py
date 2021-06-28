from rest_framework import serializers

from .models import Watchlist, StreamPlatform, Reviews


class ReviewstSerializer(serializers.ModelSerializer):
	review_user = serializers.StringRelatedField(read_only=True)

	class Meta:
		model = Reviews
		fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
	reviews = ReviewstSerializer(many=True, read_only=True)

	class Meta:
		model = Watchlist
		fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):
	watchlist = WatchListSerializer(many=True, read_only=True)

	class Meta:
		model = StreamPlatform
		fields = "__all__"
# watchlist = WatchListSerializer(many=True, read_only=True)
# watchlist = serializers.StringRelatedField(many=True)
# watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=False)
