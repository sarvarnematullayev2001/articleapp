from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment, IpModel
from django.urls import reverse_lazy

# Create your views here.
class PostListView(LoginRequiredMixin, ListView):                       
    model = Post
    template_name = 'post_list.html'

def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'post_detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        ip = get_client_ip(self.request)
        print(ip)
        if IpModel.objects.filter(ip=ip).exists():
            print("ip already present")
            post_id = self.get_object()
            print(post_id)
            post = Post.objects.get(pk=post_id.pk)
            post.views.add(IpModel.objects.get(ip=ip))
        else:
            IpModel.objects.create(ip=ip)
            post_id = self.get_object()
            post = Post.objects.get(pk=post_id.pk)
            post.views.add(IpModel.objects.get(ip=ip))
        return self.render_to_response(context)

class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('image', 'title', 'summary', 'body',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_superuser

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ('image', 'title', 'summary', 'body',)

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = 'comment.html'
    success_url = reverse_lazy('post_list')
    fields = ('post', 'comment')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    