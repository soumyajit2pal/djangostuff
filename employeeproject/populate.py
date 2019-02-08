import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","employeeproject.settings")
django.setup()

from testapp.models import *
from faker import Faker
from random import *

fakegen=Faker()

def populate(n):
    for i in range(n):
        fempno=randint(1001,9999)
        fname=fakegen.name()
        fsal=randint(10000,99999)
        faddr=fakegen.city()
        emp_record=Employee.objects.get_or_create(eno=fempno,ename=fname,esal=fsal,eaddr=faddr)
populate(30)
