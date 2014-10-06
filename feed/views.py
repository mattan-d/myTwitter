from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django import forms
from feed.models import Post
from forms import PostForm

def home(request):
    return render(request, "feed/home.html", {
        'object_list': Post.objects.order_by('-published_at').all(),
    })

def user_post(request, username):

    return render(request, "feed/user_post.html", {
        #'object_list': get_object_or_404(Post, user__username=username),
        'user_display': username,
        'object_list': Post.objects.filter(user__username=username).all(),
        'count': Post.objects.filter(user__username=username).count(),
    })

def add_post(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid:
            if request.POST['content']:
                new_post = form.save(commit=False)
                new_post.save()
                return redirect(reverse('home'))
    else:
        form = PostForm()

    return render(request, "feed/add_post.html", {
        'form': form
    })