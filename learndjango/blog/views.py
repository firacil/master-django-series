from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Blog_archive
def blog_archive(request):
    return render(request, 'blog/index.html')

# Blog_post
def blog_post(request, article_id):
    return render(request, 'blog/post.html')