from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    matriculation_Number = models.CharField(max_length=20, unique=True)


class StudentId (models.Model):
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE)


class Professor (models.Model):
    name = models.CharField(max_length=30)
    field_of_expertise = models.CharField(max_length=30)


class Semester (models.Model):
    designation = models.CharField(max_length=30)


class Course(models.Model):
    course_name = models.CharField(max_length=30)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)


class CourseDescription (models.Model):
    course_description = models.CharField(max_length=300)
    course = models.OneToOneField(Course, on_delete=models.CASCADE)
