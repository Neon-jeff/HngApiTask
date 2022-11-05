from django.db import models

# Create your models here.

class UserInput(models.Model):
    operation_type=models.CharField(max_length=100)
    num1=models.IntegerField()
    num2=models.IntegerField()

    def __str__(self):
        return self.operation