from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(110),
    ])

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.age}'
