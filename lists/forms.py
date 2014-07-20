from django import forms

class ClassForm1(forms.Form):
    the_class = forms.CharField(max_length=200)

class ClassForm2(forms.Form):
    student1 = forms.CharField(max_length=200)
    student2 = forms.CharField(max_length=200)
    student3 = forms.CharField(max_length=200)
    student4 = forms.CharField(max_length=200)
    student5 = forms.CharField(max_length=200)
