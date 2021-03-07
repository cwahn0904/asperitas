from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.
class ContFirmware(models.Model):
    name = models.CharField(
        max_length = 30,
    )
    firmware = models.FileField(
        upload_to='uploads/',
        validators=[FileExtensionValidator(allowed_extensions=['ino'])],
    )
    comment  = models.TextField(blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name