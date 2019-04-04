from django.urls import path

from . import views

urlpatterns = [
    # Основные страницы
    # path('', views.home, name='home'),
    # path('delivery/', views.delivery, name='delivery'),
    # path('pay/', views.pay, name='pay'),
    # path('equipment/', views.equipment, name='equipment'),
    # path('contacts/', views.contacts, name='contacts'),
    # path('compani/', views.compani, name='compani'),
    path('inl/', views.inl, name='inl'),
    path('optima/', views.optima, name='optima'),
    path('rio/', views.rio, name='rio'),
    path('sportage/', views.sportage, name='sportage'),
    path('default/', views.default, name='default'),


    #Шаблоны
    path('head/', views.head, name='head'),
    path('foot/', views.foot, name='foot'),
    path('calculator/', views.calculator, name='calculator'),
    path('slider/', views.slider, name='slider'),
    path('test/', views.test, name='test'),
    path('', views.default, name='default'),
]
