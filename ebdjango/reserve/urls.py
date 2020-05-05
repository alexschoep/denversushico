from django.urls import path
from . import views
from reserve.views import ReservationDetailView

urlpatterns = [
    #landing page (get)
    path('', views.index, name='index'),

    #reservation creation page (get, post)
    path('reserve/', views.reserve, name='reserve'),

    #reservation view page (get), uses generic DetailView
    path('reserve/<slug:pk>', ReservationDetailView.as_view(), name='view'),

    #reservation edit page (get, post)
    path('reserve/<slug:pk>/edit', views.edit, name='edit'),

    #reservation delete (post)
    path('reserve/<slug:pk>/delete', views.delete, name='delete')
]