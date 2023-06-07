from django.db import models


class Bot(models.Model):
    name = models.CharField(max_length=100)
    token = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'myapp_bot'

class BotTEST(models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=100)
    
