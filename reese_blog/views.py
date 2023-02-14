from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Post


# Make a variable dictionary
# posts = [
#     {
#         'author': 'Maurice Ruffin',
#         'title': 'Blog Post 1',
#         'content': 'First Post Content',
#         'date_posted': '1/31/2023'
#     },
#     {
#         'author': 'Reese Ruffin',
#         'title': 'Blog Post 2',
#         'content': 'Second Post Content',
#         'date_posted': '1/30/2023'
#     }
# ]


# Create your views here.
# Handle Routes to the websites
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'reese_blog/home.html', context)


# Make a class-base views
class PostListView(ListView):
    model = Post
    template_name = 'reese_blog/home.html'
    context_object_name = 'posts'
    # This will change the newest post to the top!
    ordering = ['-date_posted']


# Make a class-base views
class PostDetailView(DetailView):
    model = Post


# Delete a post
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # set the person(author) who created the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Post
    fields = ['title', 'content']

    # set the person(author) who created the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # Make sure that it's the RIGHT user updating their post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'reese_blog/about.html', {'title': 'about'})
