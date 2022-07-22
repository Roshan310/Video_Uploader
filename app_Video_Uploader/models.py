from pyexpat import model
from django.db import models
from django.core.validators import FileExtensionValidator
from numpy import blackman
from .validators import validate_video_size
# Create your models here.

class Video(models.Model):
    description = models.CharField(max_length=200)
    video_file = models.FileField(validators=[FileExtensionValidator(allowed_extensions=["mp4", "mkv"]), validate_video_size])
    created_at = models.DateTimeField(auto_now_add=True)
    size = models.IntegerField(null=False, blank=False)
    length = models.IntegerField(null=False, blank=True)


    def __str__(self) -> str:
        return self.description

    def charge(self, size, length):
        
        self.size = size
        self.length = length
        total_charge = 0

        if self.size < 500:
            total_charge += 5
        else:
            total_charge += 12.5
        
        if self.length < 378:
            total_charge += 12.5
        else:
            total_charge += 20
        
        return total_charge

        

    