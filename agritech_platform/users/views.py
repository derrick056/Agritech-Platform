from rest_framework import views, response
from .serializers import UserSerializer

class RegisterView(views.APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response({'message': 'User registered successfully'})
        return response.Response(serializer.errors, status=400)
