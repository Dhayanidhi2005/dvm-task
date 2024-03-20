from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bitsid = models.CharField(max_length=13,blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    class Meta:
        verbose_name_plural = "Students"