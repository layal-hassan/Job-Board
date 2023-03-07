from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Job , Apply
from django.core.paginator import Paginator
from .form import ApplyForm , JobForm , MyJobForm
from django.contrib.auth.decorators import login_required
from .filters import  JobFilter
from django.utils.text import slugify

# Create your views here.

def job_list(request):
    job_list = Job.objects.all()

    #filters
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs 

    paginator = Paginator(job_list,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'jobs':page_obj , 'myfilter':myfilter,}
    return render(request,'job/job_list.html',context)

def apply_list(request,id):
    apply_list = Apply.objects.all()
    job = Job.objects.get(id=id)
    context = {'apply_list':apply_list , 'job':job}
    return render(request,'job/apply_list.html',context)


def job_detail(request,slug):
    job_details=Job.objects.get(slug=slug)

    if request.method == 'POST':
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_details
            myform.save()
    else:
        form = ApplyForm()

    context={'job':job_details , 'form':form}
    return render(request,'job/job_details.html',context)



def my_job_list(request):
    job_list = Job.objects.all()

    context = {'myjob':job_list}
    return render(request,'job/my_job_list.html',context)

def edit_job(request , slug):
    jobs = Job.objects.get(slug = slug)
    if request.method =='POST':
        form = JobForm(request.POST , request.FILES , instance = jobs)
        if form.is_valid():
            form.save()
            return redirect('jobs:my_job_list')
    else:
        form = JobForm(instance = jobs)
    context = {'form' : form}
    return render(request,'job/edit_job.html',context)


@login_required
def add_job(request):

    if request.method == 'POST':
        form = JobForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = JobForm()

    return render(request,'job/add_job.html',{'form':form})





