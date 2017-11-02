from django.shortcuts import render

def nga(request):
    return render(request, 'nga/index.html')