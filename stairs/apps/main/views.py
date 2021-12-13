from django.shortcuts import render


def index(request):
    return render(request, 'list.html')

def calculator(request):
    return render(request, 'calculator.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def team(request):
    return render(request, 'team.html')
def about(request):
    return render(request, 'about.html')
