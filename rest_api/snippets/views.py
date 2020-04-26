from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from snippets.serializers import SnippetSerializer
from snippets.models import Snippet
from snippets.serializers import UserSerializer
from snippets.permissions import IsOwnerOrReadOnly

# Create your views here.

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SnippetSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    serializer_class = SnippetSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer