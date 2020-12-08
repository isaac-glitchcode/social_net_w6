from django.db import models
from apps.publications.models import Publication

class Comment(models.Model):
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True, null=True)
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="comments", null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering=['created_at']
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
        
    def __str__(self):
        return self.content
#proxy models