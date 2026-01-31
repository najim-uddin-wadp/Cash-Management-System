from django.db import models
from django.contrib.auth.models import AbstractUser



class AuthUserModel(AbstractUser):

    def __str__(self):
        return f"{self.username}"
    

class CashModel(models.Model):
    user=models.ForeignKey(AuthUserModel, on_delete=models.CASCADE,null=True, related_name='user_cash')
    source=models.CharField(max_length=255, null=True)
    dateTime=models.DateTimeField(null=True)
    amount=models.DecimalField(max_digits=20, decimal_places=2)
    description=models.TextField(null=True)

    def __str__(self):
        return f"{self.user.username}-{self.amount}"
    

class ExpenseModel(models.Model):
    user=models.ForeignKey(AuthUserModel, on_delete=models.CASCADE,null=True, related_name='user_expense')
    datetime=models.DateTimeField(null=True)
    amount=models.DecimalField(max_digits=20, decimal_places=2)
    description=models.TextField(null=True)

    def __str__(self):
        return f"{self.user.username}-{self.amount}"