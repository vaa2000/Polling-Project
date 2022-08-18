from django.db import models

class PollModel(models.Model):
	question = models.TextField(max_length=30)
	op1 = models.CharField(max_length=30)
	op2 = models.CharField(max_length=30)
	op3 = models.CharField(max_length=30)
	op1c = models.IntegerField(default=0)
	op2c = models.IntegerField(default=0)
	op3c = models.IntegerField(default=0)