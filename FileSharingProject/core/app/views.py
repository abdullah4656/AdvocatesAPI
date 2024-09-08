from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
class HandleFileUpload(APIView):
 def post(self,request):
  try:
    data=request.data
    serializers=FileListserializer(data=data)
    if serializers.is_valid():
        serializers.save()
        return Response({
            'status':200,
            'message':'files uploaded successfully'})
    return Response({
        'status':400,
        'message':'something went wrong',
        'data':serializers.errors
    })          
  except Exception as e:
      print(e)