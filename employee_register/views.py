from django.shortcuts import render, redirect
from .forms import EmployeeForm

#view functions
def employee_list(request):
    return render(request, "employee_register/employee_list.html")

def employee_form(request):
    #this variable will be included in employee_form.html 
    if request.method == "GET":          
        form = EmployeeForm() #empty form to rendered
        return render(request, "employee_register/employee_form.html", {'form': form})
    else:
        form = EmployeeForm(request.POST) #request.POST is  dict like object called 'QueryDict'
        if form.is_valid():
            form.save()
        return redirect('/employee/list')
        
def employee_delete(request):
    return
