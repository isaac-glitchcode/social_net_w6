from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name='Name'
        verbose_name_plural='Names'
        ordering=['name']
        
    def __str__(self):
        return self.name
        
