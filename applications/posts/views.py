from django.shortcuts import render

from . import models
from django.views import generic
# Create your views here.

class PostListView(generic.ListView):
    model = models.Post
    template_name = "posts/index.html"
    context_object_name = 'posts'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()
        return context
    

