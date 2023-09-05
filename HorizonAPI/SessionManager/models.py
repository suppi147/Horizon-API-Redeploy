from django.db import models

class UserInformation(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)
    session_openstack = models.CharField(max_length=255)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.username