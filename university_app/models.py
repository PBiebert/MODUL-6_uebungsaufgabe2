from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    matriculation_number = models.CharField(max_length=20, unique=True)


class StudentId (models.Model):
    student = models.OneToOneField(
        Student, on_delete=models.CASCADE, related_name="student_id")


class Professor (models.Model):
    name = models.CharField(max_length=30)
    field_of_expertise = models.CharField(max_length=30)


class Semester (models.Model):
    designation = models.CharField(max_length=30)


class Course(models.Model):
    course_name = models.CharField(max_length=30)
    professor = models.ForeignKey(
        Professor, on_delete=models.SET_NULL, null=True, blank=True, related_name="course_instructor")
    students = models.ManyToManyField(
        Student, related_name="enrolled_in_courses")
    semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE, related_name="semester_courses")


class CourseDescription (models.Model):
    course_description = models.CharField(max_length=300)
    course = models.OneToOneField(
        Course, on_delete=models.CASCADE, related_name="description")
