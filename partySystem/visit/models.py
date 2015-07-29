from django.db import models

# Create your models here.

class Question(models.Model):
    store=models.CharField("store app", max_length=255)
    city=models.CharField(max_length=255) 
    area=models.CharField(max_length=255) 
    vil=models.CharField(max_length=255)  
    nei=models.CharField(max_length=255)  
    rd=models.CharField(max_length=255)   
    seg=models.CharField(max_length=255)  
    lane=models.CharField(max_length=255) 
    aller=models.CharField(max_length=255)
    num=models.CharField(max_length=255)  
    f=models.CharField(max_length=255)    

    
    
#
#class Choice(models.Model):
#    question = models.ForeignKey(Question)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)