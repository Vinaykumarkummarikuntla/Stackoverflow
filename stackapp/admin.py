from atexit import register
from django.contrib import admin
from stackapp.models import Question, Comment, user

# Register your models here.
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(user)
