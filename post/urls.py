from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from post.views import PostListCreateAPIView, PostRetrieveUpdateDestroyAPIView, CommentListCreateAPIView, \
    CommentRetrieveUpdateDestroyAPIView, UserRegisterAPIView

app_name = 'post'

urlpatterns = [
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<int:pk>', PostRetrieveUpdateDestroyAPIView.as_view()),

    path('comments/', CommentListCreateAPIView.as_view()),
    path('comments/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view()),

    path('register/', UserRegisterAPIView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

]