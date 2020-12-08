from .models import Publication
from apps.tags.models import Tag
from apps.comments.models import Comment

from .serializers import PublicationSerializer
from apps.tags.serializers import TagSerializer
from apps.comments.serializers import CommentSerializer

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class PublicationsView(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    @action(methods=['GET','POST','DELETE'], detail=True)
    def tags(self, req, pk=None):
        
        publication = self.get_object()
        
        if req.method == 'GET':
            
            serializer = TagSerializer(publication.tags, many=True)
            return Response(status = status.HTTP_200_OK, data = serializer.data)
        
        if req.method in ['POST', 'DELETE']:
            
            tags_id = req.data['tags']
            
            for tag_id in tags_id:
                
                tag = Tag.objects.get(id=int(tag_id))
                
                if req.method == 'POST':
                    
                    publication.tags.add(tag)
                    return Response(status = status.HTTP_201_CREATED)
                    
                if req.method == 'DELETE':
                    try:
                        publication.tags.remove(tag)
                        return Response(status = status.HTTP_204_NO_CONTENT)
                        
                    except:
                        return Response(status = status.HTTP_400_BAD_REQUEST)
                        
    @action(methods=['GET','POST','DELETE'], detail=True)
    def comments(self, req, pk=None):
    
        publication = self.get_object()
        
        if req.method == 'GET':
            
            serializer = CommentSerializer(publication.comments, many=True)
            return Response(status = status.HTTP_200_OK, data = serializer.data)
        
        if req.method in ['POST', 'DELETE']:
    
            comments_id = req.data['comments']
            
            for comment_id in comments_id:

                comment = Comment.objects.get(id=int(comment_id))
                
                if req.method == 'POST':
                    publication.comments.add(comment)
                    return Response(status = status.HTTP_201_CREATED)
                    
                if req.method == 'DELETE':
                    try:
                        publication.comments.remove(comment)
                        return Response(status = status.HTTP_204_NO_CONTENT, data = 'Deleted')
                    except:
                        return Response(status = status.HTTP_400_BAD_REQUEST)
                    
                        