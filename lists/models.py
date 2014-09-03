from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name

class Teacher(models.Model):
    """Override the user class"""
    user = models.OneToOneField(User)
    school = models.ForeignKey(School)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    school = models.ForeignKey(School)
    teacher = models.ForeignKey(Teacher)
    students = models.ManyToManyField('Student', null=True)

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    subjects = models.ManyToManyField(Subject, null=True, blank=True)
    school = models.ForeignKey(School)

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

