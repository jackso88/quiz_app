from django.contrib import admin
from testing_apps.models import Question, Answer, Test, Cache
from django import forms

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Test)
admin.site.register(Cache)

