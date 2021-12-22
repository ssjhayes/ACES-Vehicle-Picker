from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']

class VehicleSerializer(serializers.ModelSerializer):
	Make = serializers.RelatedField()
	Model = serializers.RelatedField()
	Submodel = serializers.RelatedField()
	Year = serializers.RelatedField()

	class Meta:
		model = Vehicle
		fields = ('__all__')
