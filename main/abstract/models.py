from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

class AbstractManager(models.Manager):
    def get_by_id(self, public_id):
        try:
            instance = self.get(PublicId=public_id)
            return instance
        except (ObjectDoesNotExist, TypeError, ValueError):
            return Http404

class AbstractModel(models.Model):
    PublicId = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    objects = AbstractManager()

    class Meta:
        abstract = True



