from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Portfolio(models.Model):
    name = models.CharField(max_length=30)
    owner = models.CharField(max_length=30)
    link = models.CharField(max_length=200)
    deadline = models.DateField()
    rasm1 = models.ImageField(upload_to='media')
    rasm2 = models.ImageField(upload_to='media',null=True,blank=True)
    rasm3 = models.ImageField(upload_to='media',null=True,blank=True)
    type = models.ForeignKey(Category,on_delete=models.CASCADE)
    desc = models.TextField(null=True,blank=True)
    date = models.DateTimeField(auto_now=True)