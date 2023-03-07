from django.urls import path ,include
from . import views

app_name='job'

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),                   # jobs 
    path('fav_job/<str:slug>', views.fav_job, name='fav_job'),
    path('show_fav_job', views.show_fav_job, name='show_fav_job'),
]