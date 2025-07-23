from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def perfil(request):
    return render(request, 'perfil.html')