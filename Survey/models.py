from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class register(models.Model):
    note = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.note)
