from .models import Tag
from apps.publications.models import Publication

from .serializers import TagSerializer
from apps.publications.serializers import PublicationSerializer

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    @action(methods=['GET','POST','DELETE'], detail=True)
    def publications(self, req, pk=None):
        
        tag = self.get_object()
        
        if req.method == 'GET':
            serializer = PublicationSerializer(tag.publications, many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)