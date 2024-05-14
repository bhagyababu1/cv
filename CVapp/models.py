from django.db import models

# Create your models here.

class CV(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    place=models.CharField(max_length=200)
    mob_no=models.IntegerField()
    email=models.CharField(max_length=200)
    skills=models.CharField(max_length=5000,null=True,blank=True)
    full_name=models.CharField(max_length=200)
    date_of_birth=models.DateField()
    sex=models.CharField(max_length=200)
    nationality=models.CharField(max_length=200)
    school_attended=models.CharField(max_length=200)
    academic_qualifications=models.CharField(max_length=5000,null=True,blank=True)
    certifications=models.CharField(max_length=5000,null=True,blank=True)
    work_history=models.CharField(max_length=5000,null=True,blank=True)

    def __str__(self):
        return '{}'.format(self.name)
