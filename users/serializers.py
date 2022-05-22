from xml.parsers.expat import model
from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email']

class PostCreatorSerializer(serializers.ModelSerializer): 

    class Meta:
        model = User
        fields = ('id','username',)

