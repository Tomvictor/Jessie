from rest_framework import serializers
from core.models import *


class PostSerializer(serializers.ModelSerializer):
    timestamp = serializers.CharField(source='get_timestamp', required=False)
    last_updated = serializers.CharField(source='get_updatestamp', required=False)
    class Meta:
        model = Posts
        fields = (
            'id',
            'title',
            'content',
            'timestamp',
            'last_updated'
        )
        read_only_fields = ['id','timestamp','last_updated']



