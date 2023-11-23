from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('all_emp',views.index, name = 'all_emp'),
    path('add_emp',views.index, name = 'add_emp'),
    path('remove_emp',views.index, name = 'remove_emp'),
    path('filter_emp',views.index, name = 'filter_emp'),
]