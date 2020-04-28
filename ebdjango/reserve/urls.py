from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reserve/', views.reserve, name='reserve'),
    path('reserve/<int:resid>', views.view, name='view'),
    path('reserve/<int:resid>/edit', views.edit, name='edit')
]
