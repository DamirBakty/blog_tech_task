from rest_framework import generics, status, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from post.models import Post, Comment
from post.serializers import PostListSerializer, PostCreateUpdateSerializer, CommentSerializer, \
    CommentCreateUpdateSerializer, UserRegisterSerializer


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    permissions = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        print(self.request.user)
        if self.request.method == 'GET':
            return PostListSerializer
        return PostCreateUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permissions = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        if self.request.method == 'GET':
            return Post.objects.prefetch_related('comments')
        return Post.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return PostListSerializer
        return PostCreateUpdateSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs[self.lookup_field])
        return obj


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permissions = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        return CommentCreateUpdateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    permissions = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        if self.request.method == 'GET':
            return Comment.objects.all()
        return Comment.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentSerializer
        return CommentCreateUpdateSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=self.kwargs[self.lookup_field])
        return obj


class UserRegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permissions = [permissions.AllowAny]
