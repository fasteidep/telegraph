from django.db import models

class Okrug(models.Model):
    name = models.CharField(max_length=200)

class Uchastok(models.Model):
    namber = models.CharField(max_length=200)
    okrug = models.ForeignKey(to=Okrug, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f'{self.namber},{self.okrug}'
    
class list_Uchastkov(models.Model):
    adress = models.CharField(max_length=200)
    uchastok = models.ForeignKey(to=Uchastok, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.adress},{self.uchastok}'
    
class bith_year(models.Model):
    year = models.IntegerField()
    uchastok = models.ForeignKey(to=Uchastok, on_delete=models.CASCADE)
    
class kartochka(models.Model):
    year = models.ForeignKey(to=bith_year, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    adress = models.ForeignKey(to = list_Uchastkov, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.year},{self.first_name},{self.second_name},{self.adress}'