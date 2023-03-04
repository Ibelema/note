from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Notebook
from .serializers import NotebookSerializer
# Create your views here.
@csrf_exempt

#this is to get the list of the notebook
def notebook_list(request):
    if request.method == 'GET':
        notebooks = Notebook.objects.all()
        serializer = NotebookSerializer(notebooks, many=True)
        return JsonResponse(serializer.data, safe=False)

    #this  is to create a new notebook
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = NotebookSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return HttpResponse(serializer.errors, status=400)

#to get a single notebook and also to be able to retireve, update or delete 
@csrf_exempt
def notebook_detail(request, pk):
    try:
        notebook = Notebook.objects.get(pk=pk)
    except Notebook.DoesNotExist:
        return HttpResponse(status=404)
#retrieve 
    if request.method == 'GET':
        serializer = NotebookSerializer(notebook)
        return JsonResponse(serializer.data)
#update
    elif request.method =='PUT':
        data = JSONParser().parse(request)
        serializer = NotebookSerializer(notebook, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
#delete
    elif request.method == 'DELETE':
        notebook.delete()
        return HttpResponse(status=204)
