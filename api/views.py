

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import user_run
from .serializers import UserRunSerializer

from django.db.models import Count, Min, Sum, Avg

class UserRunList(APIView ):

  def get(self, request, format=None):
        
        userruns= user_run.objects.filter(user=request.user)

        serializer = UserRunSerializer(userruns, many=True)
        return Response(serializer.data)
  

  def post(self ,request, format=None):
     #userruns = user_run.objects.filter(user=request.user)
      user=request.user

     #serializer = UserRunSerializer(data=request.data)
      data=request.data
      userrun=user_run.objects.create(user=user,distance=data['distance'],runtime=data['runtime'])
      userrun.save()
      return Response(request.data, status=status.HTTP_201_CREATED)

class TotalRun(APIView):
  def get(self ,request, format=None):
      user=request.user
      total_distance = user_run.objects.filter(user=request.user).aggregate(total_distance=Sum('distance'))


      return Response(total_distance,status=status.HTTP_200_OK)


class AvgSpeed(APIView):
    def get(self, request, format=None):
        user = request.user
        #getting total distance
        total_distance = user_run.objects.filter(user=request.user).aggregate(total_distance=Sum('distance'))
        #getting the sum of all user run time in hours
        total_time=user_run.objects.filter(user=request.user).aggregate(total_time=Sum('runtime'))
        avgspeed=total_distance['total_distance'] /(float(total_time['total_time'])/3600)

        respose = {'AvgSpeed': avgspeed, }
        return JsonResponse(respose,status=status.HTTP_200_OK)

class AvgSessionSpeed(APIView):
    def get(self, request, pk, format=None):
        user = request.user
        userrun=user_run.objects.get(id=pk)
        avgsessionspeed = userrun.distance / (float(userrun.runtime) / 3600)

        respose = {'AvgSessionSpeed': avgsessionspeed}
        return JsonResponse(respose, status=status.HTTP_200_OK)




