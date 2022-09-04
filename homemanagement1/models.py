from django.db import models
from django.contrib import admin
from attachments.admin import AttachmentInlines


class Home(models.Model):
    home_name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.home_name



class Record(models.Model):
    record_text = models.CharField(max_length=200)
    home = models.ForeignKey(Home, on_delete=models.CASCADE)

    def __str__(self):
        return self.record_text

