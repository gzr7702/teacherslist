from django.forms import ModelForm
from django import forms 
from django.http import HttpRequest
from lists.models import Subject, Student, Teacher

class SubjectForm(ModelForm):
                    #need to filter students by school
    students = forms.ModelChoiceField(queryset=Student.objects.filter(school__name="PS222"), required=False)
    #students = forms.ModelChoiceField(queryset=Student.objects.filter(school__name=HttpRequest.user), required=False)
    class Meta:
        model = Subject
        fields = ['name', 'students']

class SignUpForm(ModelForm):
    class Meta:
        model = Teacher
        #fields = ['first_name', 'school']

