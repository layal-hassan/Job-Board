from django.urls import path ,include
from . import views
from . import api
from django.contrib.auth.models import User
app_name='job'

urlpatterns = [
    path('', views.job_list, name='job_list'),                   # jobs
    
    path('add',views.add_job,name= 'add_job'), # add job
    path('my_job_list',views.my_job_list,name= 'my_job_list'), 


    path('<str:slug>',views.job_detail,name='job_detail'),          # job details
    path('edit_job/<str:slug>',views.edit_job,name='edit_job'), 
    path('apply_list/<int:id>',views.apply_list,name='apply_list'), 

    ##  API

    path('api/jobs',api.job_list_api,name= 'job_list_api'),
    path('api/jobs/<int:id>',api.job_detail_api,name= 'job_detail_api'), 

    ## class 
    path('api/v2/jobs',api.JobListApi.as_view(),name= 'JobListApi'), 
    path('api/v2/jobs/create',api.JobCreate.as_view(),name= 'JobCreate'), 
    path('api/v2/jobs/<int:id>',api.JobDetail.as_view(),name= 'JobDetail'), 

]