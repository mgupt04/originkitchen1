from django.test import TestCase
from website.models import MenuItem 

# Create your tests here.
MenuItem.objects.all().delete()