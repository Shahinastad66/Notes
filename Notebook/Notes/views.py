from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from Notes.paginations import NotePagination
from Notes.models import Note
from Notes.serializers import NoteSerialiser
from Notes.permissions import IsOwner

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerialiser
    permission_classes = [IsAuthenticated]
    pagination_class = NotePagination
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user).order_by('created_at')
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NoteSerialiser
    permission_classes = [IsAuthenticated, IsOwner]   
    
    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)