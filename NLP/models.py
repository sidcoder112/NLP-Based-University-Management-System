from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class Course(models.Model):
    Course_Name = models.CharField(max_length=100)
    Course_code = models.CharField(max_length=100)
    Stream = models.CharField(max_length=100, default="")

class Academic_Calendar(models.Model):
    Year = models.CharField(max_length=100)
    Calendar = models.CharField(max_length=200, default="")
    COURSE=models.ForeignKey(Course, on_delete=models.CASCADE, default=1)

class Notification(models.Model):
    Notification = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    type = models.CharField(max_length=100, default="student")

class collage(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pin = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)

class Research_article(models.Model):
    Article = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Abstract = models.CharField(max_length=1000, default="")
    date  = models.CharField(max_length=100)

class subject(models.Model):
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    subject_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    credit = models.CharField(max_length=100)
    coursecode = models.CharField(max_length=100, default="")

class Exan_timetable(models.Model):
    SUBJECT = models.ForeignKey(subject, default=1, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    time = models.CharField(max_length=100)

class student(models.Model):
    COLLAGE = models.ForeignKey(collage, on_delete=models.CASCADE, default=1)
    COURSE = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    email = models.CharField(max_length=100,default=1)
    phone = models.CharField(max_length=100,default=1)

class internal_mark(models.Model):
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE, default=1)
    SUBJECT = models.ForeignKey(subject, on_delete=models.CASCADE, default=1)
    max_mark = models.CharField(max_length=100)

class External_Mark(models.Model):
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE, default=1)
    SUBJECT = models.ForeignKey(subject, on_delete=models.CASCADE, default=1)
    max_mark = models.CharField(max_length=100)

class own_list(models.Model):
    fee=models.CharField(max_length=100, default="")
    COLLEGE=models.ForeignKey(collage, on_delete=models.CASCADE)
    COURSE=models.ForeignKey(Course, on_delete=models.CASCADE)
