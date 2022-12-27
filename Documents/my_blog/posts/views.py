from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Article

# Create your views here.

#to show homepage
def homepage(request):
    return render(request, 'posts/homepage.html')

#to show all posts we do this
def posts(request):
    posts = Article.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'posts/posts.html')

#to create a post
def PostCreate(request):
    return render(request, 'posts/new_post.html')

#to edit a post
def EditPost(request, article_id):
    """Edit an existing article."""
    article = Article.objects.get(id=article_id)
   
    if request.method != 'POST':
        #initial request; pre-fill form with the current entry.
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_blog:posts', args=[posts.id]))
    context = {'posts': posts, 'article': article, 'form': form}
    return render(request, 'posts/edit.html', context)

#to create a signup message in the email
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
    
        user = User.objects.create_user(
                username = username,
                password = password,
                email = email,
            )
        login(request, user)
        subject = 'welcome to my world'
        message = f"Hi {user.username}, thank you for registering with ibelema's newsletter."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail( subject, message, email_from, recipient_list )
        return redirect('/dashboard/')
    return render(request, 'signup.html')


