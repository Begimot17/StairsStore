from django.shortcuts import render


def index(request):
    return render(request, 'list.html')


def feedback(request):
    return render(request, 'feedback.html')

def calculator(request):
    return render(request, 'calculator.html')
def gallery(request):
    return render(request, 'gallery.html')
def about(request):
    return render(request, 'about.html')
