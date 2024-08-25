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

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = "select"  
        self.fields['emp_code'].required = False