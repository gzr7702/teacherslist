from django.db import models
from django.contrib.auth.models import User

class Subject(models.Model):
    name = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    teacher = models.ForeignKey(User)
    students = models.ManyToManyField('Student', null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Parent(models.Model):
    """For now, each student has one parent to contact"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    student = models.ForeignKey(Student)

    def __str__(self):
        return self.first_name + " " + self.last_name

