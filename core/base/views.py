from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status
from .models import Advocate,Company
from .serializers import AdvocateSerializer,CompanySerializer
from rest_framework.response import Response
from django.db.models import Q
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
class AdvocateList(APIView):
    
    def get(self, request, format=None):
        Advocates = Advocate.objects.all()
        serializer = AdvocateSerializer(Advocates, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AdvocateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class AdvocateDetail(APIView):

    def get_object(self, username):
        try:
            return Advocate.objects.get(username=username)
        except Advocate.DoesNotExist:
            raise Http404
    def get(self, request, username, format=None):
        Advocate = self.get_object(username)
        serializer = AdvocateSerializer(Advocate)
        return Response(serializer.data)

    def put(self, request, username, format=None):
        Advocate = self.get_object(username)
        serializer = AdvocateSerializer(Advocate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username, format=None):
        Advocate = self.get_object(username)
        Advocate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def search(self,request):
    #  # http://127.0.0.1:8000/search/?query=Abdullah
    #     query=request.GET.get('query')
    #     if query is None:
    #      return Response({'error':'query is required'})
    #     list=Advocate.objects.filter(Q(username__icontains=query)|Q(bio__icontains=query))
    #     serializer=AdvocateSerializer(list,many=True)
    #     return Response(serializer.data)
# Create your views here.
# @api_view(['GET','POST'])
# def list_view(request):
#   if request.method=='GET':
#     list=Advocate.objects.all()
#     serializer=AdvocateSerializer(list,many=True)
#     return Response(serializer.data,status=200)
#   if request.method=="POST":
#       list=Advocate.objects.create(
#           username=request.data['username'],
#           bio=request.data['bio']
#       )
#       serializer=AdvocateSerializer(list,many=False)
#       return Response("added")
# @api_view(['GET','PUT','DELETE'])
# def Advocate_list(request,username):
#     list=Advocate.objects.get(username=username)
#     if request.method=="GET":
#      serializer=AdvocateSerializer(list,many=False)
#      return Response(serializer.data)
#     if request.method=="PUT":
#         list.username==request.data['username']
#         list.bio=request.data['bio']
#         list.save()
#         serializer=AdvocateSerializer(list,many=False)
#         return Response(serializer.data)
#     if request.method=="DELETE":
#         list.delete()
#         return Response("done")
        

# @api_view(['GET'])
# def Query(request):
#     # http://127.0.0.1:8000/search/?query=Abdullah
#     query=request.GET.get('query')
#     if query==None:
#         return Response({'error':'query is required'})
#     list=Advocate.objects.filter(Q(username__icontains=query)|Q(bio__icontains=query))
#     serializer=AdvocateSerializer(list,many=True)
#     return Response(serializer.data)
class CompanyList(APIView):
    """
    List all Companys, or create a new Company.
    """
    def get(self, request, format=None):
        query = request.GET.get('query')
        if query:
            Companys = Company.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        else:
            Companys = Company.objects.all()
        serializer = CompanySerializer(Companys, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetail(APIView):
    """
    Retrieve, update or delete a Company instance.
    """
    def get_object(self, name):
        try:
            return Company.objects.get(name=name)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        Company = self.get_object(name)
        serializer = CompanySerializer(Company)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        Company = self.get_object(name)
        serializer = CompanySerializer(Company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        Company = self.get_object(name)
        Company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class SearchAdvocates(APIView):
    def get(self, request):
        query = request.GET.get('query')
        print(f"Query parameter: {query}")
        if not query:
            return Response({'error': 'query is required'}, status=status.HTTP_400_BAD_REQUEST)
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        print(f"Advocates: {advocates}")
        serializer = AdvocateSerializer(advocates, many=True)
        return Response(serializer.data)