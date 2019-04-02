from django.shortcuts import render

# Шаблоны
def head(request):
    return render(request, 'template/head.html')

def foot(request):
    return render(request, 'template/foot.html')

def demo(request):
    return render(request, 'template/demo.html')

def calculator(request):
    return render(request, 'template/calculator.html')

def slider(request):
    return render(request, 'template/slider.html')

def test(request):
    return render(request, 'template/test.html')

# Страницы сайта
def default(request):
    return render(request, 'main/default.html')

def optima(request):
    return render(request, 'main/optima.html')

def rio(request):
    return render(request, 'main/rio.html')

def sportage(request):
    return render(request, 'main/sportage.html')

def inl(request):
    return render(request, 'main/inl.html')
