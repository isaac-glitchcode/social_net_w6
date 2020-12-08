from .models import Comment
from apps.publications.models import Publication

from .serializers import CommentSerializer
from apps.publications.serializers import PublicationSerializer

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class CommentsView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class =CommentSerializer

    @action(methods=['GET','POST','DELETE'], detail=True)
    def publications(self, req, pk=None):
        
        comment = self.get_object()
        
        if req.method == 'GET':
            
            serializer = PublicationSerializer(comment.publications)
            return Response(status = status.HTTP_200_OK, data = serializer.data)
        
        if req.method in ['POST', 'DELETE']:
            
            tags_id = req.data['tags']
            
            for tag_id in tags_id:
                
                publication = Publication.objects.get(id=int(tag_id))
                
                if req.method == 'POST':
                    
                    comment.publications.add(publication)
                    return Response(status = status.HTTP_201_CREATED)
                    
                if req.method == 'DELETE':
                    
                    comment.publications.remove(publication)
                    return Response(status = status.HTTP_204_NO_CONTENT)