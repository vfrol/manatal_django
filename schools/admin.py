from django.contrib import admin

from schools.models import School
from students.models import Student


class StudentInline(admin.TabularInline):
    model = Student
    extra = 0


class SchoolAdmin(admin.ModelAdmin):
    inlines = [StudentInline]


admin.site.register(School, SchoolAdmin)