from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from Notes.models import Note
from Notes.serializers import NoteSerialisers
from Notes.permissions import IsOwner

class NotePagination(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 10


class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerialisers
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = Note
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerialisers
    permission_classes = [IsAuthenticated, IsOwner]   
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)