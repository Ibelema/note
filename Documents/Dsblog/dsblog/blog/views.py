from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http  import HttpResponseRedirect
from .forms import PostForm
from .models import Post
# Create your views here.
def NewPost(request):
    template_name = 'NewPost.html'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post_obj = form.save(commit=False)
            post_obj.author=request.user
            post_obj.save()
            form.save()
            return HttpResponseRedirect(reverse('blog:post_list'))
    else: 
        form = PostForm()
        return render(request, template_name, {'form':form})

#this view is to obtain a single post
def post_detail(request, id):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, id=id)
    return render(request, template_name, {'post': post})

#this view is to obtain a list of our posts
def post_list(request):
    template_name='post_list.html'
    posts = Post.objects.all()
    return render(request, template_name, {'posts': posts})

#this view is for editing a post
def update_view(request, id):
    template_name = 'edit.html'
    body = {}
    obj = get_object_or_404(Post, id=id)
    form = PostForm(request.POST)
    if form.is_valid():
        post_obj = form.save(commit=False)
        post_obj.author=request.user
        post_obj.save()
        form.save()
        return HttpResponseRedirect(reverse('blog:post_list'))
    body['form'] = form
    return render(request, template_name, body)


# this view is to delete a post
def delete_view(request, id):
    template_name = 'delete.html'
    body = {}
    obj = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        obj.delete
        return HttpResponseRedirect('post')
    return render(request, template_name, body)