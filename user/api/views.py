from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class SignupToken(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['msg'] = "Testing"

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = SignupToken

@api_view(['GET'])
def get_routes(request):
    route = [
        'api/token',
        'api/token/refresh',
        'api/notes',
        'api/notes/:id',
    ]

    return Response(route,)