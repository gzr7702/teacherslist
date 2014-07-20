from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
#from django.contrib.formtools.wizard.views import SessionWizardView
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from lists import models


@login_required
def home(request):
    usr = request.user
    return render(request, 'home.html', {'user':usr})
