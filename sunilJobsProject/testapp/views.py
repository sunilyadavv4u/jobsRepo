from django.shortcuts import render
from testapp.models import HydJobs,BangJobs,PuneJobs
# Create your views here.
def home_view(request):
    return render(request,'testapp/home.html')
def hydJobs_view(request):
    jobs_list=HydJobs.objects.all()
    return render(request,"testapp/job.html",{'jobs_list':jobs_list,'jobname':'HydraBad Job'})
def puneJobs_view(request):
    jobs_list=PuneJobs.objects.all()
    return render(request,"testapp/job.html",{'jobs_list':jobs_list,'jobname':'Pune Job'})

def bangJobs_view(request):
    jobs_list=BangJobs.objects.all()
    return render(request,"testapp/job.html",{'jobs_list':jobs_list,'jobname':'Banglore Job'})
