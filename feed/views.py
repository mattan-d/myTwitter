from django.shortcuts import render, get_object_or_404
from feed.models import Post

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