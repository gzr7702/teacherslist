from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from lists import models


class Home(ListView):
    home_template = 'home.html'
    usr = 'Rob' #need to change to get user
    @login_required
    def get(self, request):
        return render(request, self.home_template, {'user':self.usr})

    def get_queryset(self):
        return models.Subject.objects.all()

class ClassWizard(SessionWizardView):
    template_name = 'classform.html'

    def create_subject(self, flist):
        return(redirect('/newformsuccess'))

    def done(self, form_list, **kwargs):
        #create students and subjects based on form_list
        self.create_subject(form_list)
        return HttpResponseRedirect('home.html')

def newformsuccess():
    pass
