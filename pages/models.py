from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserCategory(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.IntegerField()

    def __str__(self):
        return self.user
    
class VacationSlot(models.Model):
    slot = models.TextField(blank=True)
    slot_type = models.IntegerField(default=0)

    def __str__(self):
        return self.slot
    

class UserVacation(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, unique=True)
    slots = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    