from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy

from . import models, forms
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from applications.chats.models import Chat
# Create your views here.

class PostListView(generic.ListView):
    model = models.Post
    template_name = "posts/index.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        active = models.PostStatus.objects.get(status="Activa")
        return models.Post.objects.filter(status=active).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()
        context["not_found_post_message"] = "No existen publicaciones activas."
        return context

class CurrentUserPostListView(LoginRequiredMixin, PostListView):
    def get_queryset(self):
        current_user = self.request.user
        return models.Post.objects.filter(author=current_user).order_by('-update_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = models.Category.objects.all()
        context["not_found_post_message"] = "No tienes publicaciones activas."
        return context

class SearchPostByCategoryListView(PostListView):
    def get_queryset(self):
        active = models.PostStatus.objects.get(status="Activa")
        category_selected = models.Category.objects.get(name=self.kwargs['category'])
        return models.Post.objects.filter(status=active, category=category_selected)
    
class PostDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Post
    template_name = "posts/detail.html"
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Post
    form_class = forms.CreatePostForm
    template_name = "posts/add.html"
    success_url = reverse_lazy('posts:index')

    def form_valid(self, form):
        active_status = models.PostStatus.objects.get(status='Activa')
        current_user = self.request.user

        form.instance.author = current_user
        form.instance.status = active_status
        return super(PostCreateView, self).form_valid(form)

class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = models.Post
    form_class = forms.ChangePostStatusForm
    template_name = "posts/update.html"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        cancel_status = models.PostStatus.objects.get(status="Cancelada")
        if self.object.author == request.user and self.object.status != cancel_status:
            return super().dispatch(request, *args, **kwargs)
        return redirect('posts:index')

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk':self.object.pk})

class PostCancelDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Post
    template_name = "posts/cancel.html"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        cancel_status = models.PostStatus.objects.get(status="Cancelada")
        if self.object.author == request.user and self.object.status != cancel_status:
            return super().dispatch(request, *args, **kwargs)
        return redirect('posts:index')

    def get_success_url(self):
        return reverse_lazy('posts:detail', kwargs={'pk':self.object.pk})

    def delete(self, *args, **kwargs):
        cancel_status = models.PostStatus.objects.get(status="Cancelada")
        cancel_comment = self.request.POST['comment']
        self.object = self.get_object()

        self.object.cancel_comment = cancel_comment
        self.object.status = cancel_status
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class PostulationListView(LoginRequiredMixin, generic.ListView):
    model = models.Postulation
    template_name = "posts/postulations/index.html"
    context_object_name = 'postulations'
    paginate_by = 10

    def get_queryset(self):
        user = self.request.user
        return models.Postulation.objects.filter(candidate=user).order_by('-created_at')

class PostulateToPostCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Postulation
    form_class = forms.PostulateToPostForm
    template_name = "posts/postulations/postulate.html"
    success_url = reverse_lazy('posts:postulation_done')

    def dispatch(self, request, *args, **kwargs):
        post = models.Post.objects.get(pk=self.kwargs['pk'])
        current_user = self.request.user
        if post.author != current_user:
            return super().dispatch(request, *args, **kwargs)
        return redirect('posts:index')

    def form_valid(self, form):
        user = self.request.user
        evaluation = models.PostulationStatus.objects.get(status="En evaluación")
        post = models.Post.objects.get(pk=self.kwargs['pk'])

        form.instance.candidate = user
        form.instance.status = evaluation
        form.instance.post = post

        new_chat = Chat.objects.create()
        new_chat.participants.set([user, post.author])

        form.instance.chat = new_chat

        return super(PostulateToPostCreateView, self).form_valid(form)

class PostulationDoneTemplateView(LoginRequiredMixin, generic.base.TemplateView):
    template_name = 'posts/postulations/done.html'


