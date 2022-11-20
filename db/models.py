from django.db import models

# Create your models here.

from django.db import models

class DiseaseType(models.Model):
    description = models.CharField(max_length=140)
    def __str__(self):
        return self.description 

class Country(models.Model):
    cname = models.CharField(max_length=50, unique= True) 
    population = models.BigIntegerField()
    
    def __str__(self):
        return self.cname 

class  Disease(models.Model):
    diseaseCode = models.CharField(unique=True, max_length=50)
    pathogen = models.CharField(max_length=20)
    description = models.CharField(max_length=140)
    id_dt = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.diseaseCode 
    
class  Discover(models.Model):
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    diseaseCode = models.ForeignKey(Disease, on_delete=models.CASCADE)
    firstEncDate = models.DateField()
    
    class Meta:
        unique_together = ['cname', 'diseaseCode']

class  Users(models.Model):
    email = models.CharField(max_length=60, unique=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=40)
    salary = models.IntegerField()
    phone = models.CharField(max_length=20)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.email 
    
class  PublicServant(models.Model):
    email = models.ForeignKey(Users, on_delete=models.CASCADE, unique=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.email 
    
class  Doctor(models.Model):
    email = models.ForeignKey(Users, on_delete=models.CASCADE, unique=True)
    degree = models.CharField(max_length=20)

    def __str__(self):
        return self.email 
    
    
class  Specialize(models.Model):
    diseaseType = models.ForeignKey(DiseaseType, on_delete=models.CASCADE)
    email = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['diseaseType', 'email']
    
    def __str__(self):
        return self.email.email.email
        
class  Record(models.Model):
    email = models.ForeignKey(PublicServant, on_delete=models.CASCADE)
    cname = models.ForeignKey(Country, on_delete=models.CASCADE)
    diseaseCode = models.ForeignKey(Disease, on_delete=models.CASCADE)
    totalDeath = models.IntegerField()
    totalPatients = models.IntegerField()
    
    class Meta:
        unique_together = ['email', 'cname','diseaseCode']