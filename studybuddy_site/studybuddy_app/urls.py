from django.urls import path
from .views import user as user_views
from .views import meetup as meetup_views
from .views import review_list
from .views.meetup import MeetupListView
from .views.meetup import MeetupDetailView
app_name = "studybuddy_app"

urlpatterns = [

    path("meetups/<int:pk>/rsvp/", meetup_views.rsvp, name="meetup.rsvp"),
    path("meetups/<int:pk>/cancel_participation/", meetup_views.cancel_participation, name="meetup.cancel_participation"),

    path("meetups/<int:pk>/", MeetupDetailView.as_view(), name="meetup.detail"),
    path("meetups", MeetupListView.as_view(), name="meetup.list"),

    path("meetups/new", meetup_views.new, name="meetup.new"),
    path("meetups/<int:pk>/delete", meetup_views.delete, name="meetup.delete"),
    path("meetups/<int:pk>/edit", meetup_views.edit, name="meetup.edit"),

    path("", MeetupListView.as_view(), name="index"),

    path("users/<int:pk>", user_views.detail, name="user.detail"),

    path('reviews/', review_list.ReviewListView.as_view(), name='review_list'),
]

# https://restfulapi.net/
# https://apiguide.readthedocs.io/en/latest/build_and_publish/use_RESTful_urls.html

# list: GET /meetups
# create meetup: POST /meetups

# single meetup: GET /meetups/:id
# update meetup: PUT(POST) /meetups/:id - django does only support GET and POST
# delete meetup: DELETE /meetups/:id

# new form: GET /meetups/new
# edit form: GET /meetups/:id/edit
