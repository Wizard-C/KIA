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

def inl(request):
    return render(request, 'main/inl.html')
