from django.db import models
from cabinet.models import Cabinet
from django.contrib.auth.models import User


class Time(models.Model):
    start = models.CharField('Start time', max_length=255)
    end = models.CharField('End time', max_length=255)

    def __str__(self):
        return f"{self.start} - {self.end}"

    class Meta:
        verbose_name = "Time"
        verbose_name_plural = "Times"


class Course(models.Model):
    name = models.CharField('Course name', max_length=255)
    code = models.CharField('Course code', max_length=255)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    time = models.ForeignKey(Time, on_delete=models.CASCADE)
    week_day = models.IntegerField('Week', default=0)
    type = models.CharField('Course type', max_length=255, default='')
    type_code = models.CharField('Course type code', max_length=255, default='')


    def __str__(self):
        return self.code + ' - ' + self.name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lesson.name} - {self.user.username}"

    class Meta:
        verbose_name = "Schedule"
        verbose_name_plural = "Schedules"


class LessonChanged(models.Model):
    lesson = models.ForeignKey(Course, on_delete=models.CASCADE)
    new_time = models.ForeignKey(Time, on_delete=models.CASCADE)
    new_cab = models.ForeignKey(Cabinet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Changed{self.lesson.name}"

    class Meta:
        verbose_name = "Changed lesson"
        verbose_name_plural = "Changed lessons"
        

class Message(models.Model):
    title = models.TextField("Title")
    content = models.TextField("Content")
    date = models.DateTimeField('Time')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Message"
        verbose_name_plural = "Messages"

#already read messages
class ReadMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.message.title}"

    class Meta:
        verbose_name = "Read message"
        verbose_name_plural = "Read messages"

