from .models import Addition
from .serializers import AdditionSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AdditionView(APIView):

	def get(self,request):
		additions = Addition.objects.all()
		serializer = AdditionSerializer(additions, many=True)
		return Response(serializer.data)

	def post(self,request):
		serializer = AdditionSerializer(data=request.data)
		if serializer.is_valid(raise_exception=True):
			entry=serializer.save()
			if entry.operation == '+':
				return Response({"Result": "{}".format(entry.num1+entry.num2)}, status=status.HTTP_201_CREATED)
			elif entry.operation == '-':
				return Response({"Result": "{}".format(entry.num1-entry.num2)}, status=status.HTTP_201_CREATED)
			else:
				return Response("Enter either '+' or '-' symbols in operation field!")
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


