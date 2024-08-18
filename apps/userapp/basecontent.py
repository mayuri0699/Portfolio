from django.db import models

class BaseContent(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    last_updated_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True