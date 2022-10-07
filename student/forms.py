from django import forms

class StudForm(forms.Form):
    s_name = forms.CharField(max_length = 30)
    s_class = forms.CharField(max_length = 30)
    s_address = forms.CharField(max_length = 30)
    s_school = forms.CharField(max_length = 30)
    s_email = forms.CharField(max_length = 30)
    
    
class SForm(forms.Form):
    s_name = forms.CharField(max_length = 30)
    