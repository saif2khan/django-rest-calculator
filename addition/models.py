from django.db import models

class Addition(models.Model):
	num1 = models.IntegerField()
	num2 = models.IntegerField()
	operation = models.CharField(max_length=1,default=0)


