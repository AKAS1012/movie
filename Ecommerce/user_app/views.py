from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import RegisterSerializer


# Create your views here.
@api_view(['POST'])
def registration_view(request):
	if request.method == "POST":
		serializer = RegisterSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
