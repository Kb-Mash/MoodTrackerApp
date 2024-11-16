from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
        path('api/user/', views.UserCreateView.as_view()),
        path('api/token/', jwt_views.TokenObtainPairView.as_view(),name='token_obtain_pair'),
        path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
        path('api/mood/', views.MoodListCreateView.as_view()),
        path('api/mood/<int:pk>/', views.MoodDetailView.as_view()),
        path('api/notes/', views.NotesListCreateView.as_view()),
        path('api/notes/<int:pk>/', views.NotesDetailView.as_view()),
]
