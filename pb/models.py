from django.db import models

class Pastebin(models.Model):
    text = models.TextField(default="")
    id = models.TextField(default="", primary_key=True)
