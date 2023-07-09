from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Meetup, Review


# admin.site.register(Meetup)

class MeetupAdmin(admin.ModelAdmin):
    # fields = ["location", "title", "start_time", "end_time"]

    fieldsets = [
        ("What?", {"fields": ["title"]}),
        ("When?", {"fields": ["start_time", "duration"]}),
        ("Where?", {"fields": ["location"]}),
    ]
    list_display = ["title", "start_time"]


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Title:", {"fields": ["title"]}),
        ("Rating:", {"fields": ["rating"]}),
        ("Description:", {"fields": ["review"]}),
    ]
    list_display = ["title", "date"]


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Review, ReviewAdmin)
