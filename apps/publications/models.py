from django.db import models
from apps.tags.models import Tag

class Publication(models.Model):
    public_status = models.BooleanField(default=False, null=True)
    content = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag, related_name='publications', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering=['created_at']
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
        
    def __str__(self):
        return self.content
        
    
    
    
