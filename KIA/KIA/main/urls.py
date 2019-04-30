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
    path('inl_demo/', views.inl_demo, name='inl_demo'),

    path('main/', views.main, name='main'),
    path('main/<int:Car_model_inl_id>/', views.interior_main, name='interior_main'),

    #Шаблоны
    # path('head/', views.head, name='head'),
    # path('foot/', views.foot, name='foot'),
    # path('calculator/', views.calculator, name='calculator'),
    # path('slider/', views.slider, name='slider'),
    # path('test/', views.test, name='test'),
    # path('callback/', views.callback, name='callback'),
    # path('thank/', views.thank, name='thank'),
]
