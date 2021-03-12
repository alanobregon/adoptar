from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms
from . import models
# Create your views here.
class ChatListView(LoginRequiredMixin, generic.ListView):
    model = models.Chat
    template_name = "chats/index.html"
    context_object_name = 'chats'

    def get_queryset(self):
        return models.Chat.objects.filter(participants=self.request.user).order_by('-id')

class ChatDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Chat
    template_name = "chats/messages.html"
    context_object_name = 'chat'

    def dispatch(self, request, *args, **kwargs):
        chat = self.get_object()
        evaluation = 'En evaluación'

        if chat.postulation.status.status == evaluation and self.request.user in chat.participants.all():
            return super().dispatch(request, *args, **kwargs)
        return redirect('chats:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = forms.SendMessageForm
        return context
    
    def post(self, request, *args, **kwargs):
        form = forms.SendMessageForm(request.POST, request.FILES)
        if form.is_valid:
            current_user = self.request.user
            current_chat = self.get_object()

            form.instance.chat = current_chat
            form.instance.sender = current_user

            form.save()

            self.object = self.get_object()
            context = super(ChatDetailView, self).get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context=context)