from django.contrib import admin

# Register your models here.
from . models import Person,Student

admin.site.register(Person)
admin.site.register(Student)