from rest_framework import serializers
from eventapi.models import Event

class EventSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'date', 'created_at', 'updated_at','title', 'description', 'image_url']
        read_only_fields = ['id', 'created_at', 'updated_at']