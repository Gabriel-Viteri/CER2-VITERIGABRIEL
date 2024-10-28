from django.db import models

class user(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    mail = models.EmailField()

    def __str__(self) -> str:
        return self.username
