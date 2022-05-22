from rest_framework import serializers

from post.models import Post as PostModel

class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostModel
        fields = '__all__'
