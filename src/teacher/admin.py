from django.contrib import admin
from .models import Rate
from .models import Rating
from .models import RateCache
from .models import Comment

admin.site.register(Rate)
admin.site.register(Rating)
admin.site.register(RateCache)
admin.site.register(Comment)
