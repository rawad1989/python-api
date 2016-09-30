from django.contrib.auth import authenticate, login as auth_login
from rest_framework.response import Response
from django.http import HttpResponse, HttpResponseBadRequest
from django.http import JsonResponse
from rest_framework.authtoken.models import Token

import  json

def login(request):

    if request.method=='POST':
        data = json.loads(request.body.decode("utf-8"))
        username = data['username']
        password = data['password']
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                #checking if user is active
                if user.is_active:

                    token = Token.objects.create(user=user)
               #     request.session.set_expiry(300) #limitting the session to only 5 mins
                    content = {
                   'success' : True ,
                   'key' : token
                    }
                else:
                    content = {'success': False, 'error': 'User is not active'}
            else:
                content = {
                'success': False,
                'error': 'Wrong username or password'
                }
        return JsonResponse(content)
    return HttpResponseBadRequest()






