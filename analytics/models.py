from django.db import models

# Create your models here.
class Analytics(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    page_visited = models.CharField(max_length=200, blank=True, default='')
    user_action = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.page_visited