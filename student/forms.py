from cProfile import label
from django import forms

class StudForm(forms.Form):
    s_name = forms.CharField(max_length = 30, label="Student Name ")
    s_class = forms.CharField(max_length = 30, label="Student Class ")
    s_address = forms.CharField(max_length = 30, label="Student Address")
    s_school = forms.CharField(max_length = 30, label="School Name")
    s_email = forms.CharField(max_length = 30, label= "Email")
    
    
class SForm(forms.Form):
    s_name = forms.CharField(max_length = 30)
    