from email.policy import default
from django.db import models

class Filepdf(models.Model):
    id = models.AutoField
    title = models.CharField(max_length=150,default = "")
    file = models.FileField(upload_to='filePDF/',default = "")
    disc = models.CharField(max_length=600,default = "")
    category = models.CharField(max_length=100,default="")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title