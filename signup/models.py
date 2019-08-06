from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    emailid = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='pictures/', null = True, blank = True)


    def __str__(self):
        return self.name
