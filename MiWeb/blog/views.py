from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog(request):
    VPost = Post.objects.all()    # Importe todo los objetos que le indicamos en el modelos,py
    return render(request, 'blog/blog.html', {"post" : VPost})

