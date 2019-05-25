from django.contrib import admin
from .models import MotherEntity, EntityType

# Register your models here.
admin.site.register(MotherEntity)
admin.site.register(EntityType)
