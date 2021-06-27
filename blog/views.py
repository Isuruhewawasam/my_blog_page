from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, catgory
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
class home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']


class Post_details(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        stuff =get_object_or_404(Post, id= self.kwargs['pk'])
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        context =super(Post_details,self).get_context_data()
        total_likes =stuff.total_likes()
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context


class Add_post(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class Add_Category(CreateView):
    model = catgory
    template_name = 'category.html'
    fields = '__all__'


class Update_post(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class Delete_post(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_details', args=[str(pk)]))