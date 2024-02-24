from django.shortcuts import render

def index(request):
    context = {
        'title': 'Cinema',
        'content': 'Здесь будет какой-то контент...',
    }
    return render(request, 'main/index.html', context)
def profile(request):
    return render(request, 'main/profile.html')

def theaters(request):
    return render(request, 'main/theaters.html')

def upcoming(request):
    return render(request, 'main/upcoming.html')

def promotions(request):
    return render(request, 'main/promotions.html')

def news(request):
    return render(request, 'main/news.html')