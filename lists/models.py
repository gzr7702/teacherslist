from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Subject(models.Model):
    name = models.CharField(max_length=200)
    students = models.ManyToManyField(Student, null=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    subjects = models.ForeignKey(Subject)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Parent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.first_name + " " + self.last_name
