from django.shortcuts import render
from blog.models import Post, Categorias

# Create your views here.
def blog(request):
    VPost = Post.objects.all()    # Importe todo los objetos que le indicamos en el modelos,py
    return render(request, 'blog/blog.html', {"post" : VPost})

def vistaCategoria(request, categorias_id):
    VarCategoria = Categorias.objects.get(id=categorias_id)  # Obtiene la categoría con el id proporcionado
    VPost = Post.objects.filter(categorias=VarCategoria)  # Filtra los posts que pertenecen a esa categoría
    return render(request, "blog/categorias.html", {'VistaCategoria': VarCategoria, 'post' : VPost })