from django.db import models
from django.contrib.auth.models import User

class Rate(models.Model):
    rate_id = models.BigAutoField(primary_key=True)
    rate_text = models.TextField('Rate Text')

    def __str__(self):
        return self.rate_text

    class Meta:
        verbose_name = "Rate"
        verbose_name_plural = "Rates"

class Rating(models.Model):
    rating_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='given_ratings', on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, related_name='received_ratings', on_delete=models.CASCADE)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
    rate_value = models.IntegerField('Rate Value')

    def __str__(self):
        return str(self.rate_value)

    class Meta:
        verbose_name = "Rating"
        verbose_name_plural = "Ratings"

class RateCache(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.ForeignKey(Rate, on_delete=models.CASCADE)
    overall = models.FloatField('Overall')
    count = models.IntegerField('Count', default=0)

    def __str__(self):
        return str(self.overall)

    class Meta:
        verbose_name = "Rate Cache"
        verbose_name_plural = "Rate Caches"

class Comment(models.Model):
    comment_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='given_comments', on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, related_name='received_comments', on_delete=models.CASCADE)
    content = models.TextField('Content')
    date = models.DateTimeField('Date')
    block = models.BooleanField('Block')

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
