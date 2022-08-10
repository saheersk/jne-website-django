from django.contrib import admin
from web.models import CollegeDetail, CollegeNew, Contact, Course, Developer, LatestEvent, Testimonial


class CollegeDetailAdmin(admin.ModelAdmin):
    list_display = ("title",)

admin.site.register(CollegeDetail, CollegeDetailAdmin)


class CollegeNewAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "event_date")

admin.site.register(CollegeNew, CollegeNewAdmin)


class LatestEventAdmin(admin.ModelAdmin):
    list_display = ("title", "event_date")

admin.site.register(LatestEvent, LatestEventAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = ("course", "title")

admin.site.register(Course, CourseAdmin)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "name", "designation", "company")

admin.site.register(Testimonial, TestimonialAdmin)


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ("name", "designation")

admin.site.register(Developer, DeveloperAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "cap_id", "course", "dob", "gender", "father_name", "mother_name", "downloaded_date")

admin.site.register(Contact, ContactAdmin)