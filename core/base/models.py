from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def  __str__(self):
        return self.name

# Create your models here.
class Advocate(models.Model):
    company=models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=100)
    bio=models.TextField(null=True,blank=True)
    img=models.ImageField(upload_to="images",blank=True)
    followers=models.IntegerField(default=0)
    twitterlink=models.CharField(max_length=300,default="")
    def __str__(self):
        return self.username