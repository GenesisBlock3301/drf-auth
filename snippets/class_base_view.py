from rest_framework import permissions
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Snippet
from .modelSerializer import SnippetSerializer,UserSerializer
from django.contrib.auth.models import User


class SnippetListView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self,request,format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        data =  self.request.data
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=404)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class SnipperDetail(APIView):
    """
    retrieve update delete and snipper instance
    """
    def get_object(self,pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,formate=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

