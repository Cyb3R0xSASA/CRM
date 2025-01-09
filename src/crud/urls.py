from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('logout', views.logout, name='logout'),
    path('records', views.record, name='records'),
    path('record/<int:record_id>', views.view_record, name='record'),
    path('record_edit/<int:record_id>', views.edit_record, name='record_edit'),
    path('delete_record/<int:record_id>', views.delete_record, name='delete_record'),
    path('search', views.search, name='search')
]