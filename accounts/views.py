from django.contrib.auth import authenticate, login
from django.core.checks import messages
from django.shortcuts import redirect, render
from .forms import SignupForm , UserForm ,ProfileForm
from .models import Profile
from django.urls import reverse
from job.models import Job
# Create your views here.  
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username='username', password='password')
            # login(request, user)
            return redirect('/accounts/login')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'form':form})



def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html',{'profile':profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform= ProfileForm(request.POST,request.FILES, instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))
    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})


def fav_job(request,slug):
    if request.user.is_authenticated and not request.user.is_anonymous  :
        fav = Job.objects.get(slug=slug)
        if Profile.objects.filter(user=request.user,fav_job=fav).exists():
            profile= Profile.objects.get(user=request.user)
            profile.fav_job.remove(fav)  
        else:
            profile= Profile.objects.get(user=request.user)
            profile.fav_job.add(fav)  
    else:
        return redirect('/jobs/' + slug)
    return redirect('/jobs/' + fav.slug)


def show_fav_job(request):
    context = None
    if request.user.is_authenticated and not request.user.is_anonymous:
        userInfo = Profile.objects.get(user=request.user)
        job = userInfo.fav_job.all()
        context = {'jobs':job}
    return render(request,'job/my_jobs.html',context)

