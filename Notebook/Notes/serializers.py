from rest_framework import serializers
from Notes.models import Note

class NoteSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ['user', 'created_at']