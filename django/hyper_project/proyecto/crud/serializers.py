#Importacion de los serializers
from rest_framework import serializers 
from .models import CrudUser

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = CrudUser 
    fields = '__all__'
