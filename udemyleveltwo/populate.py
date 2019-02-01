import django
import os
 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","udemyleveltwo.settings")
django.setup()

from testapp.models import User
from faker import Faker

fakegen=Faker()
def populate(n=5):
    for i in range(n):
        fake_name=fakegen.name().split(" ")
        fake_firstname=fake_name[0]
        fake_lastname=fake_name[1]
        fake_email=fakegen.email()

        user=User.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,email=fake_email)
if __name__ == "__main__":
    print("Populating database")
    populate(10)
    print("ya complete")