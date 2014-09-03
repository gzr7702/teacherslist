from django.conf.urls import patterns, include, url

from lists import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#from lists.forms import ClassForm1, ClassForm2
#from lists.views import ClassWizard, Home

urlpatterns = patterns('',
    url(r'^$', 'lists.views.home'),
    #url(r'^classform', ClassWizard.as_view([ClassForm1, ClassForm2])),
    #url(r'^newformsuccess', views.newformsuccess, name='newformsuccess'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
