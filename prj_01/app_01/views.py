from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post, Response
from .forms import PostForm, ResponseForm


class PostList(ListView):
    model = Post
   # ordering = '-dateCreation'
    template_name = 'post.html'
    context_object_name = 'post'
    paginate_by = 10


class PostUpdate(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'
    success_url = '/post/'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class ResponseList(LoginRequiredMixin, ListView):
    form_class = ResponseForm
    model = Response
    template_name = 'response.html'
    context_object_name = 'response'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['UserResponse'] = Response.objects.filter(author=self.request.user)
        return context


class ResponseCreate(LoginRequiredMixin, CreateView):
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'
    success_url = '/post/'

    def form_valid(self, form):
        response = form.save(commit=False)
        response.author = self.request.user
        response.save()
        return super().form_valid(form)


class ResponseDelete(DeleteView):
    model = Response
    template_name = 'response_delete.html'
    success_url = '/response/'
