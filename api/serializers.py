from rest_framework import  serializers
from .models import user_run

class UserRunSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = user_run
        fields = ('id','distance','runtime')

