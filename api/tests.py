from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from django.core.management import call_command
from api.models import user_run
import  json
import  os



class API_Test(TestCase):



    fixtures = ['fixtures/initial_data.json']


    def setUp(self):

        self.user = User.objects.create_user( username='test', email='yre@123.com', password='test')
        self.user.save()

    #testing login to the api
    def test_login(self):

        client = APIClient()
        user = self.user
        request = client.post('/api/login/', {'username': 'test','password':'test'}, format='json')

        response = request
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.render().content)
        self.user.save()

    #testing add user run
    def test_adduserrun(self):
        client = APIClient()
        user = User.objects.get(username='test1')
        token = Token.objects.get(user=user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request = client.post('/api/userrun/', {'distance': '100', 'runtime': '3600'}, format='json')
        self.assertEqual(request.status_code, 201)
        self.assertEqual(request.render().content, '{"distance":"100","runtime":"3600"}')


    def test_userrun(self):

        client = APIClient()
        user = User.objects.get(username='test1')
        token = Token.objects.get(user=user)

        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request = client.get('/api/userrun/')
        #  print request
        json_response = json.loads(request.render().content)

        self.assertEqual(request.status_code, 200)

    def test_avgSpeed(self):
        client = APIClient()
        user=User.objects.get(username='test2')
        token =Token.objects.get(user=user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request=client.get('/api/avgspeed/')
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.content, '{"AvgSpeed": 8.992506244796003}')


    def test_totalRun(self):
        client = APIClient()
        user = User.objects.get(username='rawad')
        token = Token.objects.get(user=user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request = client.get('/api/totalrun/')
        json_reponse= json.loads(request.render().content)
        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.render().content,'{"total_distance":100}')

    def test_avgSessionSpeed(self):
        client = APIClient()
        user = User.objects.get(username='test1')
        userrun= user_run.objects.filter(user=user)
        #get the avrage for the first session
        userrunid=userrun.first().id

        token = Token.objects.get(user=user)
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        request = client.get('/api/avgsessionspeed/'+`userrunid`)


        self.assertEqual(request.status_code, 200)
        self.assertEqual(request.content , '{"AvgSessionSpeed": 100.0}')

