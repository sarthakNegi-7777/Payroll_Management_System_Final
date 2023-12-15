from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('login_page/',views.login_page, name = 'login_page'),
    path('',views.index, name = 'index'),
    path('all_emp',views.all_emp, name = 'all_emp'),
    path('add_emp',views.add_emp, name = 'add_emp'),
    path('remove_emp',login_required(views.remove_emp), name = 'remove_emp'),
    path('remove_emp/<int:emp_id>',views.remove_emp, name = 'remove_emp'),
    path('filter_emp',views.filter_emp, name = 'filter_emp'),

    path('emp_added_success/', views.emp_added_success, name='emp_added_success'),
    path('emp_removed_success/', views.emp_removed_success, name='emp_removed_success'),
    path('signout', views.signout, name = 'signout'),
    path('About', views.About, name = 'About'),


] 