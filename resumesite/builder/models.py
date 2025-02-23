from django.db import models

class Resume(models.Model):
  first_name = models.CharField(max_length=100, null=True)
  last_name = models.CharField(max_length=100, null=True)
  city = models.CharField(max_length=50, null=True)
  country = models.CharField(max_length=50, null=True)
  pin_code = models.IntegerField(null=True)
  #Educational Information
  degree = models.CharField(max_length=100, null=True)
  eduField = models.CharField(max_length=50, null=True)
  eduCity = models.CharField(max_length=50, null=True)
  Institute = models.CharField(max_length=100, null=True)

class WorkExpModel(models.Model):
  role = models.CharField(max_length=100, null=True)
  company = models.CharField(max_length=50, null=True)
  timePeriod = models.CharField(max_length=50, null=True)
  workDesc = models.CharField(max_length=500, null=True)
  resume = models.ForeignKey(Resume, related_name='work_experiences', on_delete=models.CASCADE)

class Interest(models.Model):
  interestDesc = models.CharField(max_length=50, null=True)
  resume = models.ForeignKey(Resume, related_name='interests', on_delete=models.CASCADE)


