from .models import MoodEntry, NotesEntry
from .serializers import UserSerializer, MoodSerializer, NotesSerializer
from rest_framework import permissions, generics
from django.contrib.auth import get_user_model


class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    permission_classes = [
            permissions.AllowAny
    ]

    serializer_class = UserSerializer


class MoodListCreateView(generics.ListCreateAPIView):
    serializer_class = MoodSerializer
    permission_classes = [
            permissions.IsAuthenticated
    ]

    def get_queryset(self):
        queryset = MoodEntry.objects.filter(user=self.request.user)
        created_at = self.request.query_params.get('date', None)
        if created_at is not None:
            queryset = queryset.filter(created_at=created_at)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MoodDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoodEntry.objects.all()
    serializer_class = MoodSerializer
    permission_classes = [
            permissions.IsAuthenticated
    ]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class NotesListCreateView(generics.ListCreateAPIView):
    serializer_class = NotesSerializer
    permission_classes = [
            permissions.IsAuthenticated
    ]

    def get_queryset(self):
        queryset = NotesEntry.objects.filter(user=self.request.user)
        created_at = self.request.query_params.get('date', None)

        if created_at is not None:
            queryset = queryset.filter(created_at=created_at)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NotesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NotesEntry.objects.all()
    serializer_class = NotesSerializer
    permission_classes = [
            permissions.IsAuthenticated
    ]

    def perform_update(self, serializzer):
        serializer.save(user=self.request.user)
