from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin


class PostListView(ListView):
    model = Posts
    template_name = 'blog_app/home.html'
    context_object_name = 'posts'
    ordering = ['-date_created']
    paginate_by = 3

class PostDetailView(DetailView):
    model = Posts
    template_name = 'blog_app/post-details.html'

def about(request):
    return render(request,'blog_app/about.html')


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Posts
    template_name = 'blog_app/post-create.html'
    fields = ['title','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Posts
    template_name = 'blog_app/post-create.html'
    fields = ['title','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False

        
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Posts
    template_name = 'blog_app/post-delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False
    
