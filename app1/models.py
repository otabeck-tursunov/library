from django.db import models

class Student(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=10)
    bitiruvchi = models.BooleanField()
    kitob_soni = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.ism


class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    tirik = models.BooleanField(default=True)
    kitob_soni = models.PositiveSmallIntegerField()
    tugilgan_yil = models.DateField()
    def __str__(self):return self.ism

class Kitob(models.Model):
    nom = models.CharField(max_length=70)
    sahifa = models.PositiveSmallIntegerField()
    janr = models.CharField(max_length=30)
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    olingan_sana = models.DateField(null = True, blank=True)
    qaytardi = models.BooleanField(default=False)
    qaytargan_sana = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"{self.student.ism}, {self.kitob.nom}"




