from django.shortcuts import render

from rest_framework import generics,status
from .serializers import GuidesSerializer
from .models import guide
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.
# class GuidesView(viewsets.ModelViewSet):
#     serializer_class = GuidesSerializer
#     queryset = guide.objects.all()



# class LoginView(APIView):
#     serializer_class = LoginSerializer
#     # for_post_request
#     def post(self,request,format=None):
#         serilaizer = self.serializer_class(data=request.data)
#         if serilaizer.is_valid():
#             email = serilaizer.data.get('email')
#             password = serilaizer.data.get('password')
#             queryset = guide.objects.filter(email=email)
#             if queryset.exists():
#                 return Response(GuidesSerializer(guide).data,status=status.HTTP_200)



    
