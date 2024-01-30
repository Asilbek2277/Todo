from django.db import models

class Student(models.Model):
    ism=models.CharField(max_length=20)
    yosh=models.PositiveSmallIntegerField()
    kurs=models.PositiveSmallIntegerField()
    Student_raqami=models.PositiveSmallIntegerField(unique=True)


    def __str__(self):
        return f"{self.ism}"

class Rejalar(models.Model):
    sarlavha=models.CharField(max_length=40)
    sana=models.DateField()
    batafsil_malumot=models.CharField(max_length=100, null=True, blank=True)
    bajarilgan=models.BooleanField()
    Student=models.ForeignKey(Student, on_delete=models.CASCADE)


    def __str__(self):
        return f"{self.sarlavha}"


