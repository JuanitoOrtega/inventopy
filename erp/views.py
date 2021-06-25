from django.shortcuts import render

# Create your views here.
def myfirstview(request):
    data = {
        'name': 'Juanito Ortega'
    }
    return render(request, 'index.html', data)
