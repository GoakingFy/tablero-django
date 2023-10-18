from django.shortcuts import render
from .forms import PostForm

# Create your views here.

def indexpage(request):
    return render(request, 'buscaminas/index.html', {})

def table_new(request):
    form = PostForm()
    return render(request, 'buscaminas/index.html', {'form': form})