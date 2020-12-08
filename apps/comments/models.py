from django.db import models
from apps.publications.models import Publication
# from apps.users.models import User

class Comment(models.Model):
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True, null=True)
    publications = models.ForeignKey(Publication, on_delete=models.CASCADE)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now_add=True, null=True)
    
    class Meta:
        ordering=['created_at']
        verbose_name = 'Content'
        verbose_name_plural = 'Content'
        
    def __str__(self):
        return self.content
