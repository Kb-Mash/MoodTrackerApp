from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import MoodEntry, NotesEntry


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
                username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ('pk', 'username', 'password')


class MoodSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = MoodEntry
        fields = ('pk', 'mood', 'created_at', 'user')


class NotesSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = NotesEntry
        fields = ('pk', 'notes', 'created_at', 'user')
