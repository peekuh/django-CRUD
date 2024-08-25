from django import forms    
from .models import Employee
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('emp_code', 'fullname', 'mobile', 'position')
        labels = {
            'fullname' :  'Full Name',
            'emp_code'  :  'employee code'
        }

