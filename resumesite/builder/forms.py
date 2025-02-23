from django import forms

class PersonalInformationForm(forms.Form):
  first_name = forms.CharField(label='First Name', max_length=100)
  last_name = forms.CharField(label='Last Name', max_length=100)
  city = forms.CharField(label='city', max_length=50)
  country = forms.CharField(label='country', max_length=50)
  pin_code = forms.IntegerField()

class EducationInformationForm(forms.Form):
  degree = forms.CharField(label='Degree', max_length=100)
  eduField = forms.CharField(label='Education FIeld', max_length=50)
  eduCity = forms.CharField(label='city', max_length=50)
  Institute = forms.CharField(label='Institute', max_length=100)
  
class WorkExperienceForm(forms.Form):
  role = forms.CharField(label='Role', max_length=100)
  company = forms.CharField(label='Company', max_length=50)
  timePeriod = forms.CharField(label='timePeriod', max_length=50)
  workDesc = forms.CharField(label='Work Description', max_length=500)


class InterestForm(forms.Form):
  interestDesc = forms.CharField(label='Interest', max_length=50)

