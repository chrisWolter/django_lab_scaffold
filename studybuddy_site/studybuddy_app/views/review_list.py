from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from studybuddy_app.models import Review


class ReviewListView(LoginRequiredMixin, generic.ListView):
    model = Review
    template_name = 'studybuddy_app/review_list.html'
    context_object_name = 'review_list'
