from django.contrib import admin
from lists.models import Parent, Subject, Student, School, Teacher

admin.site.register(Parent)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Teacher)

#class TeacherAdmin(admin.ModelAdmin):
#    def save_model(self, request, obj, form, change):
#        obj.user = request.user
#        obj.save()
