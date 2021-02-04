from django.db import models
from . import views


class User(models.Model):
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Favorites(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    api_id = models.IntegerField()

    # def __str__(self):
    #     return self.title




