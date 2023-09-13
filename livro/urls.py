from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exemplo/<int:id>', views.exemplo, name='exemplo'),
    path('livros', views.livros, name='livros'),
]
