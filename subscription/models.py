from django.db import models

# Create your models here.
class Subscription(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    email_address = models.CharField(max_length=100, blank=True, default='')
    user_message = models.TextField(blank=True, default='')
    user_cellnumber = models.CharField(max_length=100, blank=True, default='')

    class Meta:
        ordering = ['created']

    def __str__(self):
        return str(self.id) + " - " + self.email_address