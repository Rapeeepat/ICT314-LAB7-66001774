from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.student_id
