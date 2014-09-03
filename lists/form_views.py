from django.shortcuts import render_to_response
from django.forms.models import modelformset_factory
from django.core.context_processors import csrf
from django.template import RequestContext
from lists.forms import SubjectForm, SignUpForm

def signup(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        new_teacher = form.save(commit=False)
        new_teacher.save()
    return render_to_response('signup.html', locals(), context_instance=RequestContext(request))

def create_subject(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        new_subject = form.save(commit=False)
        #add teacher and school by grabbing them from request.User
        new_subject.teacher = request.user
        new_subject.teacher = request.user.school #does this work?
        new_subject.save()
    return render_to_response('subform.html', locals(), context_instance=RequestContext(request))

def create_student(request):
    pass

def create_parent(request):
    pass

#def create_subject(request):
#    SubjectFormSet = modelformset_factory(Subject, fields=("name", "students"))
#    if request.method == "POST":
#        formset = SubjectFormSet(request.POST)
#        if formset.is_valid():
#            formset.save()
#            print("data saved")
            # Do something.
#    else:
#        formset = SubjectFormSet(queryset=Subject.objects.filter(name__startswith='O'))
#    return render_to_response("subform.html", {"formset": formset,}, context_instance=RequestContext(request))
