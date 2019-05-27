from django.shortcuts import render

posts = [
    {
        'author': 'Elnaz Dehkharghani',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'May 27, 2019'
    },
    {
        'author': 'Hassan Ghorbani',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'May 28, 2019'
    }
]

def home(request):
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

