from django.db import models


class TGUserModel(models.Model):
    tg_id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    objects = models.Manager()
