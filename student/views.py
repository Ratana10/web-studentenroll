from django.shortcuts import render

from student.forms import SForm, StudForm
from .models import stud

# Create your views here.
def index(request):
    return render(request, "student/home.html")

def register(request):
    title = "Student Registeration"
    form = StudForm(request.POST or None)
    
    if form.is_valid():
        name = form.cleaned_data['s_name']
        clas = form.cleaned_data['s_class']
        address = form.cleaned_data['s_address']
        school = form.cleaned_data['s_school']
        email = form.cleaned_data['s_email']
        
        #check if email already exist ==> student already register
        exit_email = stud.objects.filter(s_email = email)
        if len(exit_email) > 0 :
            return render(request, "student/ack.html", {'title':'email already register !!'})
            
        
        #s = stud(s_name="teest", s_class = "teest", s_address="teest", s_school="teest", s_email="teest")
        s = stud(s_name=name, s_class = clas, s_address=address, s_school=school, s_email=email)
        s.save()   # save this data into database
        return render(request, "student/ack.html", {'title':'Registered successfully'})


    context = {
        'title' : title,
        'form'  : form,
    }
    return render(request, "student/register.html", context)


def existing(request):
    title = 'All Registered Students'
    # get all student register
    query_set = stud.objects.all()
    
    context ={
        'title' : title,
        'queryset' : query_set,
    }
    return render(request, "student/existing.html", context)


def search(request):
    title = 'Search Student'
    form = SForm(request.POST or None)
    
    if form.is_valid():
        name = form.cleaned_data['s_name']
        queryset = stud.objects.filter(s_name = name)
        if len(queryset) == 0 :
            return render(request, "student/ack.html", {'title' : 'Student not found ....'})    
            
        context = {
            'title' : title,
            'queryset'  : queryset,
        }
        return render(request, "student/existing.html", context)    

    #display the black if doesn't have the data
    context = {
        'title' : title,
        'form'  : form,
    }

    return render(request, "student/search.html", context)
    

def dropout(request):
    title = 'Dropout Student'
    form = SForm(request.POST or None)
    
    if form.is_valid():
        name = form.cleaned_data['s_name']
        queryset = stud.objects.filter(s_name = name)
        
        if len(queryset) == 0 :
            return render(request, "student/ack.html", {'title' : 'Student not found ....'})    

        else:
            queryset = stud.objects.filter(s_name = name).delete()
            return render(request, "student/ack.html", {'title' : 'Student remove form database'})    
     

    #display the black if doesn't have the data
    context = {
        'title' : title,
        'form'  : form,
    }

    return render(request, "student/dropout.html", context)
    
    