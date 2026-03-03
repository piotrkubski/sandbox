from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    FormView,
    View
)
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, logout
from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'is_published']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(is_published=True).order_by('-published_date') #mozna zamiast orderby dodac class Meta do modelu z glopbalnym sortowaniem


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'is_published']
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        post = self.object
        return reverse('blog:post_detail', kwargs={'pk': post.pk})


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'blog/login.html'
    success_url = reverse_lazy('blog:post_list') #blog:post_list z urls

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('blog:post_list')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
