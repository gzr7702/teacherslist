from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse, HttpResponseRedirect
#from django.template import RequestContext, loader
#from django.contrib.formtools.wizard.views import SessionWizardView
#from django.views.generic import ListView
from lists.models import Subject

@login_required
def home(request):
    usr = request.user
    if usr is not None:
        subs = Subject.objects.filter(teacher=usr)
        return render_to_response('home.html', {'usr':usr, 'subs':subs})
    else:
        return render_to_response('sign_up.html')
