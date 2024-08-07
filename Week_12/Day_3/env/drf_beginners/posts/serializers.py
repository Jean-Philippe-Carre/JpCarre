from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('custom_id', 'title', 'category', 'content',
                  'publish_date', 'last_updated')
