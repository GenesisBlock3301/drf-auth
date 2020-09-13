from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework.decorators import api_view


@api_view(['GET','POST'])
def snippet_list(request,format=None):
    """
    list all snippet
    :param request:
    :return:
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

    if request.method == "GET":
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets,many=True)
        # for i in serializer.data:
        #     print(i['code'])
        return JsonResponse(serializer.data,safe=False)

@api_view(['GET','PUT','DELETE'])
def snippet_detail(request,pk):
    """
    receive , update or delete code snippet
    :param requesr:
    :param pk:
    :return:
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serilizer = SnippetSerializer(snippet)
        return JsonResponse(serilizer.data,safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serilizer = SnippetSerializer(snippet,data=data)
        return HttpResponse(serilizer)

    elif request.method == "DELETE":
        snippet.delete()
        return HttpResponse(snippet)

