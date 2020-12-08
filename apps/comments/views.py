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
    def publication(self, req, pk=None):
        
        comment = self.get_object()
        
        if req.method == 'GET':
            
            serializer = PublicationSerializer(comment.publication)
            return Response(status = status.HTTP_200_OK, data = serializer.data)
