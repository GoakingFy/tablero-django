from django.shortcuts import render
from .forms import tableForm


# Create your views here.

def indexpage(request):
   table_form = tableForm()
   return render(request, 'buscaminas/index.html', {'table_form': table_form})



   