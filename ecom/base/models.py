from django.db import models
import uuid

class BaseModel(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    
    
    class Meta:
        abstract = True # so that django doesn't this as a model but it will treat as a class so we can use it in etire project


