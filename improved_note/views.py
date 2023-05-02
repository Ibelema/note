from rest_framework import status
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notebook
from .serializers import NotebookSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def notebook_list(request):
    if request.method == 'GET':
        notebooks = Notebook.objects.all()
        serializer = NotebookSerializer(notebooks, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NotebookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#to get a single notebook and also to be able to retireve, update or delete 
@api_view(['GET', 'PUT', 'DELETE'])
def notebook_detail(request, pk):
    try:
        notebook = Notebook.objects.get(pk=pk)
    except Notebook.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#retrieve 
    if request.method == 'GET':
        serializer = NotebookSerializer(notebook)
        return Response(serializer.data)
#update
    elif request.method =='PUT':
        serializer = NotebookSerializer(notebook, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#delete
    elif request.method == 'DELETE':
        notebook.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
