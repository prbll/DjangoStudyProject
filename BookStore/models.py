from django.db import models
import uuid


# Create your models here.
class MotherEntity(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    LastModifiedDateTime = models.DateTimeField(auto_now=True)
    Type = models.ForeignKey('EntityType', on_delete=models.CASCADE)

    def __str__(self):
        return self.Title


class EntityType(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    TypeName = models.CharField(max_length=100)

    def __str__(self):
        return self.TypeName
