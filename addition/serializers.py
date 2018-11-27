from rest_framework import serializers
from .models import Addition

class AdditionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Addition
		fields = ('num1','num2','operation')
		