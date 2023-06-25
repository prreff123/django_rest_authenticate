from django.contrib import admin
from .models import student,Book,Category
# Register your models here.

admin.site.register(student)
admin.site.register(Book)
admin.site.register(Category)
