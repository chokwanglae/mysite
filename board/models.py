from django.db import models

# Create your models here.
from user.models import User


class Board(models.Model):
    title=models.CharField(max_length=200)
    content =models.CharField(max_length=2000)
    hit = models.IntegerField(default=0)
    regedate = models.DateTimeField
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Board(%s,%s,%d,%s,%d)" % (self.title, self.content, self.hit, str(self.regedate), self.user.id)

