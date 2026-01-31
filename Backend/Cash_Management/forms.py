from django import forms
from.models import CashModel, ExpenseModel



class CashForm(forms.ModelForm):
    class Meta:
        model=CashModel
        fields='__all__'
        exclude=['user']
        widgets={
            'dateTime':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model=ExpenseModel
        fields='__all__'
        exclude=['user']
        widgets={
            'datetime':forms.DateTimeInput(attrs={'type':'datetime-local'})
        }
        

