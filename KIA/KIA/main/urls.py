from django.urls import path

from . import views

urlpatterns = [
    # Основные страницы
    path('', views.default, name='default'),
    path('inl/', views.inl, name='inl'),
    path('optima/', views.optima, name='optima'),
    path('rio/', views.rio, name='rio'),
    path('sportage/', views.sportage, name='sportage'),
    path('default/', views.default, name='default'),

    #Шаблоны
    # path('head/', views.head, name='head'),
    # path('foot/', views.foot, name='foot'),
    # path('calculator/', views.calculator, name='calculator'),
    # path('slider/', views.slider, name='slider'),
    # path('test/', views.test, name='test'),
    # path('callback/', views.callback, name='callback'),
    # path('thank/', views.thank, name='thank'),
]
