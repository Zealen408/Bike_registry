from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from.serializers import *

from bikes.models import bike

class bikeViewAPI(generics.ListAPIView):
    queryset = bike.objects.filter(bike_stolen=True)
    serializer_class = bikeSerializer

# class bikeListUserView(APIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes = [IsAuthenticated]
#     def get(self, request, format=None):
#         content = {
#             'user': request.user,  # `django.contrib.auth.User` instance.
#             'auth': request.auth,  # None
#         }
#         return Response(content)

