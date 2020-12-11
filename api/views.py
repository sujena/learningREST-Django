from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DataSerializer
from .models import Info
# Create your views here.

@api_view (['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/data-list/',
        'Detail View': '/data-detail/<str:pk>/',
        'Create': '/data-create/',
        'Update': '/data-update/<str:pk>',
        'Delete': '/data-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view (['GET'])
def dataList(request):
    data1= Info.objects.all()
    serializer= DataSerializer(data1, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def dataDetail(request,pk):
    try:
        data1 = Info.objects.get(iata=pk)
        serializer= DataSerializer(data1, many=False)
    except:
        data1 = Info.objects.get(name=pk)
        serializer= DataSerializer(data1, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def dataCreate(request):
    serializer= DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def dataUpdate(request, pk):
    try:
        data1 = Info.objects.get(iata=pk)
        serializer= DataSerializer(instance=data1, data=request.data)
        if serializer.is_valid():
            serializer.save()
    except:
        data1 = Info.objects.get(name=pk)
        serializer = DataSerializer(instance=data1, data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def dataDelete(request, pk):
    try:
        data1 = Info.objects.get(iata=pk)
        data1.delete()
    except:
        data1 = Info.objects.get(name=pk)
        data1.delete()
    return Response("Item deleted")

