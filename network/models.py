from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Repo(models.Model):
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=128)
    link =  models.CharField(max_length=128)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="repos", null=True)

    def __str__(self):
        return f"{self.id}: name = {self.name}; desc = {self.desc}; link = {self.link}"

class Tag(models.Model):
    name = models.CharField(max_length=64)
    repo = models.ManyToManyField(Repo, blank=False, related_name = "tags")
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tags", null=True)

    def __str__(self):
        return f"{self.id}: name: {self.name}"

