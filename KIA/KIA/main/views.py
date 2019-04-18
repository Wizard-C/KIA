from django.shortcuts import render

from main.models import Car_model_inl
# callback form

# from .forms import NameForm
#
# def get_name ( request ):
#     # create a form instance and populate it with data from the request:
#     form = Call_back ( request.POST )
#     # check whether it's valid:
#     if form.is_valid ():
#         # process the data in form.cleaned_data as required
#         # ...
#         # redirect to a new URL:
#         return HttpResponseRedirect ( '/thanks/' )
#     return render ( request , 'name.html' , { 'form' : form })
#
# def callback(request):
#     return render(request, 'template/callback.html')
#
# def thank(request):
#     return render(request, 'template/thank.html')


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
def inl_demo(request):
    list_car = {'cars': Car_model_inl.objects.all()}
    return render(request, 'main/demo_inl.html', list_car)


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
