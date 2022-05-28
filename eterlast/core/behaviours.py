from django.db import models

from model_utils.models import TimeStampedModel
import uuid


class UUIDMixin(TimeStampedModel):
    id = models.UUIDField(default=uuid.uuid4, editable=False, db_index=True, primary_key=True)

    class Meta:
        abstract = True