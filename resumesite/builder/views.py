from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PersonalInformationForm, EducationInformationForm, WorkExperienceForm, InterestForm
from .models import Resume, WorkExpModel, Interest
from django.urls import reverse

def index(request):
  return render(request, 'index.html')

def personalInfo(request):

  if(request.method == "POST"):
    form1 = PersonalInformationForm(request.POST)
    form2 = EducationInformationForm(request.POST)
    form3 = WorkExperienceForm(request.POST)
    form4 = InterestForm(request.POST)

    print(request.POST)

    resObj = Resume.objects.get(pk=1)
    resObj.first_name = request.POST['first_name']
    resObj.last_name = request.POST['last_name']
    resObj.city = request.POST['city']
    resObj.country = request.POST['country']
    resObj.pin_code = request.POST['pin_code']
    resObj.degree = request.POST['degree']
    resObj.eduField = request.POST['eduField']
    resObj.eduCity = request.POST['eduCity']
    resObj.Institute = request.POST['Institute']
    resObj.save()

    workexpObj = WorkExpModel.objects.get(pk=1)
    workexpObj.role = request.POST['role']
    workexpObj.company = request.POST['company']
    workexpObj.timePeriod = request.POST['timePeriod']
    workexpObj.workDesc = request.POST['workDesc']
    workexpObj.save()

    interestObj = Interest.objects.get(pk=1)
    interestObj.interestDesc = request.POST['interestDesc']
    interestObj.save()
    
    # interest1 = Resume.objects.get(pk=1)
    # interest2 = Resume.objects.get(pk=2)


    return HttpResponseRedirect(reverse('resume-page'))

  else:
    form1 = PersonalInformationForm()
    form2 = EducationInformationForm()
    form3 = WorkExperienceForm()
    form4 = InterestForm()
    
  context = {
    'form1' : form1,
    'form2' : form2,
    'form3' : form3,
    'form4' : form4
  }

  return render(request, 'personalInfo.html', context)

def resumePage(request):
  resObj = Resume.objects.get(pk=1)

  first_name = resObj.first_name
  last_name = resObj.last_name
  city = resObj.city
  country = resObj.country
  pin_code = resObj.pin_code
  degree = resObj.degree
  eduField = resObj.eduField
  eduCity = resObj.eduCity
  institute = resObj.Institute

  workexpObj = WorkExpModel.objects.get(pk=1)
  role = workexpObj.role
  company = workexpObj.company
  timePeriod = workexpObj.timePeriod
  workDesc = workexpObj.workDesc
  
  interestObj = Interest.objects.get(pk=1)
  interestDesc = interestObj.interestDesc

  context = {
    'first_name' : first_name,
    'last_name' : last_name,
    'city' : city,
    'country' : country,
    'pin_code' : pin_code,
    'degree' : degree,
    'eduField' : eduField,
    'eduCity' : eduCity,
    'institute' : institute,
    'role' : role,
    'company' : company,
    'timePeriod' : timePeriod,
    'workDesc' : workDesc,
    'interestDesc' : interestDesc
  }

  return render(request, 'resumePage.html', context)