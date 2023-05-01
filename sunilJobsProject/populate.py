import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sunilJobsProject.settings')
import django
django.setup()
from faker import Faker
from random import *
from testapp.models import HydJobs
fake=Faker()
def phonenumberGenerator():
    d1=choice("6789")
    for i in range(9):
        d1=d1+str(randint(0,9))
    return d1
['date','company','Title','eligibility','address','email','phonenumber']
def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Project Manager','Team Lead',"software Engineer",'Associate Engineer','System Analyst'))

        feligibility=fake.random_element(elements=("B.Tech","M.Tech",'MCA','Phd','B.Sc'))
        faddress=fake.address()
        femail=fake.email()
        fphonenumber=phonenumberGenerator()

        hyd_job_record=HydJobs.objects.get_or_create(date=fdate,
              company=fcompany,
              Title=ftitle,
              eligibility=feligibility,
              address=faddress,
              email=femail,
              phonenumber=fphonenumber)


n=int(input("Enter Numbers of Record-:"))
populate(n)
print(f"{n} Record Inserted succesfully..")
