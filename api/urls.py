from django.conf.urls import  include ,url

from . import views








urlpatterns = [
    url(r'^totalrun/$', views.TotalRun.as_view()),
    url(r'^userrun/$', views.UserRunList.as_view()),
    url(r'^avgspeed/$', views.AvgSpeed.as_view()),
    url(r'^avgsessionspeed/(?P<pk>[0-9]+)$', views.AvgSessionSpeed.as_view()),

    
]