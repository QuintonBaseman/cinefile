from django.contrib.auth.models import User, Group
from rest_framework import serializers, permissions

from user_accounts.models import Favorites

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ('user', 'api_id')

class UserSerializer(serializers.ModelSerializer):
    # favorites = FavoritesSerializer()
    # favorite_list = serializers.RelatedField(source='favorites', read_only=True)
    favorites_set = FavoritesSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'favorites_set')

