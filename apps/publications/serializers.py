from rest_framework import serializers
from apps.publications.models import Publication
from apps.tags.models import Tag
from apps.tags.serializers import TagSerializer
from apps.comments.models import Comment
from apps.comments.serializers import CommentSerializer


# class CommentSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Comment
#         fields = '__all__'
        
# class TagSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Tag
#         fields = '__all__'
        
class PublicationSerializer(serializers.ModelSerializer):
    tags = TagSerializer(Tag, read_only=True, many=True)
    comments = CommentSerializer(Comment, read_only=True, many=True)
    class Meta:
        model = Publication
        fields = '__all__'
