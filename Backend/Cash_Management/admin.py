from django.contrib import admin
from .models import AuthUserModel, CashModel, ExpenseModel

admin.site.register(AuthUserModel)
admin.site.register(CashModel)
admin.site.register(ExpenseModel)