from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from Cash_Management.forms import CashForm,ExpenseForm
from django.db.models import Sum


def Register_Page(request):
    if request.method=='POST':
        un=request.POST.get('username')
        em=request.POST.get('email')
        pw=request.POST.get('password')
        cpw=request.POST.get('confirm_password')

        user_exist=AuthUserModel.objects.filter(username=un).exists()
        if user_exist:
            messages.error(request, 'User Already Exists! Try Another One')
            return redirect('Register_Page')
        
        if pw==cpw:
            AuthUserModel.objects.create_user(
                username=un,
                email=em,
                password=pw,    
            )
            messages.success(request, 'Registration Successfull')
            return redirect('LogIn_Page')

    return render (request, 'auth/register.html')

def LogIn_Page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'welcome! you login successfully')
            return redirect('LandingPage')
        
        else:
            messages.success(request, 'Wrong Attempt')
            return redirect('LogIn_Page')


    return render(request, 'auth/login.html')

def LogOut(request):
    logout(request)
    return redirect('LogIn_Page')

def ChangePassword(request):
    current_user=request.user
    if request.method=='POST':
        old_pw=request.POST.get('old_password')
        new_pw=request.POST.get('new_password')
        conf_new_pw=request.POST.get('confirm_new_password')

        if check_password(old_pw, current_user.password):
            if new_pw==conf_new_pw:
                current_user.set_password(new_pw)
                current_user.save()
                messages.success(request, 'change password successfull!')
                return redirect('LogIn_Page')
            
    return render(request, 'auth/changepassword.html')


@login_required
def LandingPage(request):
    total_cash=CashModel.objects.filter(user=request.user).aggregate(total_cash_amount=Sum('amount'))['total_cash_amount'] or 0
    total_expenses=ExpenseModel.objects.filter(user=request.user).aggregate(total_expense_amount=Sum('amount'))['total_expense_amount'] or 0
    total_balance= total_cash-total_expenses
    context={
        'total_cash':total_cash,
        'total_expenses':total_expenses,
        'total_balance':total_balance,
    }
    return render(request, 'landingpage.html', context)


def  Transactions(request):
    data1=CashModel.objects.filter(user=request.user)
    data2=ExpenseModel.objects.filter(user=request.user)

    context={
        'data1':data1,
        'data2':data2,
    }
    return render(request, 'transaction.html', context)



#----------------cash model section-------------
@login_required
def AddCash(request):
    if request.method=='POST':
        cash_form=CashForm(request.POST)
        if cash_form.is_valid():
            cash_data=cash_form.save(commit=False)
            cash_data.user=request.user
            cash_data.save()
            return redirect('CashList')

    else:
        cash_form=CashForm()

    context={
        'cash_form':cash_form,
        'title':'Add Cash Info',
        'button':'Add Cash',
    }
    
    return render(request, 'cash/addcash.html',context)


def Edit_Cash(request, pk):
    edit_data=CashModel.objects.get(id=pk)
    if request.method=='POST':
        cash_form=CashForm(request.POST, instance=edit_data)
        if cash_form.is_valid():
            cash_data=cash_form.save(commit=False)
            cash_data.user=request.user
            cash_data.save()
            return redirect('CashList')

    else:
        cash_form=CashForm(instance=edit_data)

    context={
        'cash_form':cash_form,
        'title':'Edit Cash Info',
        'button':'Update Info',
    }
    
    return render(request, 'cash/addcash.html',context)

def delete_cash(request,pk):
    CashModel.objects.get(id=pk).delete()
    return redirect('CashList')


def CashList(request):
    list_data=CashModel.objects.filter(user=request.user)

    context={
        'list_data':list_data
    }

    return render(request, 'cash/cashlist.html', context)


#----------------------Expenses Section----------------------------
@login_required
def Expense_list(request):
    list_data=ExpenseModel.objects.filter(user=request.user)

    context={
        'list_data':list_data
    }
    return render(request, 'expense/expense_list.html', context)


def Expense_Add(request):
    if request.method=='POST':
        Expense_form=ExpenseForm(request.POST)
        if Expense_form.is_valid():
            expense_info=Expense_form.save(commit=False)
            expense_info.user=request.user
            expense_info.save()
            return redirect('Expense_list')

    else:
        Expense_form=ExpenseForm()

    context={
        'Expense_form':Expense_form,
        'title':'Add Expenses',
        'button':'Click To Add'
    }
    return render(request, 'expense/expense_add.html', context)



def Edit_Expense_Add(request, pk):
    edit_data=ExpenseModel.objects.get(id=pk)
    if request.method=='POST':
        Expense_form=ExpenseForm(request.POST, instance=edit_data)
        if Expense_form.is_valid():
            expense_info=Expense_form.save(commit=False)
            expense_info.user=request.user
            expense_info.save()
            return redirect('Expense_list')

    else:
        Expense_form=ExpenseForm(instance=edit_data)

    context={
        'Expense_form':Expense_form,
        'title':'Add Expenses',
        'button':'Click To Add'
    }
    return render(request, 'expense/expense_add.html', context)

def Delete_exp_list(request,pk):
    ExpenseModel.objects.get(id=pk).delete()
    return redirect('Expense_list')