from django.contrib import admin
from .models import Time, Course, Schedule, LessonChanged, Message, ReadMessage
# Register your models here.

admin.site.register(Time)
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(LessonChanged)
admin.site.register(Message)
admin.site.register(ReadMessage)
