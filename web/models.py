import datetime

from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


COURSE = (
    ("bca", "BCA"),
    ("bba", "BBA"),
    ("bcom", "BCOM"),
    ("ba-english", "BA-ENGLISH"),
    ("bsc-physics", "BSC-PHYSICS"),
    ("mcom", "MCOM"),
    ("msc-physics", "MSC-PHYSICS"),
)

GENDER = (
    ("male", "MALE"),
    ("female", "FEMALE"),
    ("other", "OTHER"),
)


class CollegeDetail(models.Model):
    icon = models.CharField(max_length=150)
    count = models.CharField(max_length=50)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class CollegeNew(models.Model):
    image = models.ImageField(upload_to="News_image/")
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateField()

    def __str__(self):
        return self.title


class LatestEvent(models.Model):
    image = models.ImageField(upload_to="Latest_event/")
    title = models.CharField(max_length=250)
    event_date = models.DateField()

    def __str__(self):
        return self.title


class Course(models.Model):
    course = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    year = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    image = models.ImageField(upload_to="Testimonial/")
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    company = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Developer(models.Model):
    image = models.ImageField(upload_to="Developer/")
    name = models.CharField(max_length=150)
    designation = models.CharField(max_length=150)
    linkedin_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    cap_id = models.CharField(max_length=50)
    course = models.CharField(max_length=128, choices=COURSE)
    dob = models.DateField()
    gender = models.CharField(max_length=128, choices=GENDER)
    student_number = PhoneNumberField()
    father_name = models.CharField(max_length=128)
    mother_name = models.CharField(max_length=128)
    parent_number = PhoneNumberField()
    institution = models.CharField(max_length=128)
    month_and_year =  models.CharField(max_length=128)
    course_selected_for_plus_two = models.CharField(max_length=128)
    percentage_obtained = models.CharField(max_length=128)
    downloaded_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name
