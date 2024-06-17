from django.contrib import admin
from django.urls import path
from . import views 
urlpatterns = [
    path('fruits/', views.index,name='home'),
    path('search/',views.search_fruits,name='search'),
    path('delete_fruit/<int:fruit_id>/', views.delete_fruit, name='delete_fruit'),
    path('add_fruit/', views.add_fruit, name='add_fruit'),
    path('update_fruit/<int:fruit_id>/', views.update_fruit, name='update_fruit'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

]   