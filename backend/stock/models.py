from django.db import models

# Create your models here.

class Stocks(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    checkBuyValue = models.IntegerField(default=9999999999)
    checkSellValue = models.IntegerField(default=0)
    