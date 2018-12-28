from rest_framework import serializers
from core.models import *


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = (
            'id',
            'title',
            'content',
            'timestamp',
            'last_updated'
        )
        read_only_fields = ['id']