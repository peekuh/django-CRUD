from django.shortcuts import render
from .forms import EmployeeForm

def employee_list(request):
    return render(request, "employee_register/employee_list.html")

def employee_form(request):
    #this variable will be included in employee_form.html 
    form = EmployeeForm() #empty form to rendered
    return render(request, "employee_register/employee_form.html", {'form': form})

def employee_delete(request):
    return
