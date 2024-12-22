from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Blog_archive
def blog_archive(request):
    
    # get articles from the database
    # pass it to render to dynamically pass it to our page
    
    blog_post = [
        {'id': 1, 'title': 'The Importance of Time Management', 'author': 'Firaol Mk', 'content': 'Learn how to manage your time effectively to boost productivity and reduce stress.', 'date': 'December 15, 2024' },
        {'id': 2, 'title': '5 Tips for Staying Motivated', 'author': 'Ebisa N', 'content': 'Discover actionable tips to keep yourself motivated, even on challenging days.', 'date': 'April 01, 2024' },
        {'id': 3, 'title': 'The Benefits of Journaling', 'author': 'Yisak O', 'content': 'Explore how maintaining a journal can enhance your personal growth and mindfulness.', 'date': 'January 01, 2025' },
        {'id': 4, 'title': 'My Learning Journey at ALX', 'author': 'Firaol Mk', 'content': 'talk about how i tackle projects when i am in ALX software engineering program.', 'date': 'November 14, 2024' }
    ]
    
    context = {"list_of_post": blog_post}
    return render(request, 'blog/index.html', context)

# Blog_post
def blog_post(request, article_id):
    return render(request, 'blog/post.html')