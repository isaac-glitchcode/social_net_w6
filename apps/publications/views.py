from .models import Publication
from apps.tags.models import Tag

from .serializers import PublicationSerializer
from apps.tags.serializers import TagSerializer

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
                    
                    publication.tags.remove(tag)
                    return Response(status = status.HTTP_204_NO_CONTENT)