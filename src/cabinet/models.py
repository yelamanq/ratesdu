from django.db import models


# Create your models here.

class Cabinet(models.Model):
    name = models.CharField('Lesson name', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Cabinet"
        verbose_name_plural = "Cabinets"


class CabinetStatus(models.Model):
    caption = models.CharField('Status', max_length=255)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = "Cabinet status"
        verbose_name_plural = "Cabinet statuses"


class CabinetStatusValue(models.Model):
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE)
    cabinet_status = models.ForeignKey(CabinetStatus, on_delete=models.CASCADE)
    value = models.IntegerField('Status value')

    def __str__(self):
        return self.cabinet.name

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"
