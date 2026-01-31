from django.urls import path
from .views import *

urlpatterns=[
    path('',Register_Page, name='Register_Page'),
    path('LogIn_Page/',LogIn_Page, name='LogIn_Page'),
    path('LandingPage/',LandingPage, name='LandingPage'),
    path('LogOut/',LogOut, name='LogOut'),
    path('ChangePassword/',ChangePassword, name='ChangePassword'),
    path('Transactions/',Transactions, name='Transactions'),


    #----------------cash---------------------
    path('AddCash/',AddCash, name='AddCash'),
    path('Edit_Cash/<int:pk>/',Edit_Cash, name='Edit_Cash'),
    path('delete_cash/<int:pk>/',delete_cash, name='delete_cash'),
    path('CashList/',CashList, name='CashList'),

    #------------expenses----------------
    path('Expense_list/', Expense_list, name='Expense_list'),
    path('Expense_Add/',Expense_Add , name='Expense_Add'),
    path('Edit_Expense_Add/<int:pk>/',Edit_Expense_Add , name='Edit_Expense_Add'),
    path('Delete_exp_list/<int:pk>/',Delete_exp_list , name='Delete_exp_list'),


]
