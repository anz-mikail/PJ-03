from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView
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


class ResponseList(LoginRequiredMixin, ListView):
    form_class = ResponseForm
    model = Response
    template_name = 'response.html'


class ResponseCreate(LoginRequiredMixin, CreateView):
    form_class = ResponseForm
    model = Response
    template_name = 'response_create.html'


