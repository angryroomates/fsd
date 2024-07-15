from django.db import models

class stud(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    #date_joined=models.DateField()
    def __str__(self):
        return f"{self.fname}{self.lname}"
    
class course(models.Model):
    course_name=models.CharField(max_length=40)
    student=models.ManyToManyField(stud,related_name="enrollment")

    def __str__(self):
        return self.course_name