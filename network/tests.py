from django.test import TestCase, Client
from .models import Repo, User

# Create your tests here.

class RepoTestCase(TestCase):

    def setUp(self):

        Repo.objects.create(name="Test Object", desc="A little test", link="wwww.test.ts", tag="test")
        Repo.objects.create(name="Test Object2", desc="A little test", link="wwww.test.ts", tag="test")
        Repo.objects.create(name="Test Object3", desc="A little test", link="wwww.test.ts", tag="test")

       

    
