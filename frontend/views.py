
from django.shortcuts import render
import requests
import json
from api.views import dataDetail

# Create your views here.
def searchBox(request):
    return render(request, 'search.html')

def searchData(request):
    if request.method == 'GET':
        pk = request.GET.get('pk', False)
        print(pk)
        url= 'http://127.0.0.1:8000/api/data-detail/'+pk
        response = requests.get(url).json()
        return render(request, 'data.html', {'data': [response]})

def viewList(request):
    response=requests.get('http://127.0.0.1:8000/api/data-list').json()
    return render(request, 'data.html', {'data': response})

def createData(request):
    if request.method == 'POST':
        pk2 = request.POST.get('pk2', False)
        print(pk2)
        pk22=json.loads(pk2)
        url= 'http://127.0.0.1:8000/api/data-create/'
        response = requests.post(url, data=pk22).json()
        return render(request, 'data.html', {'data': [response]})

def updateData(request):
    if request.method == 'POST':
        pk4 = request.POST.get('pk4', False)
        pk5 = request.POST.get('pk5', False)
        pk55=json.loads(pk5)
        print (pk55)
        url= 'http://127.0.0.1:8000/api/data-update/'+pk4+'/'
        response = requests.post(url, data=pk55).json()
        return render(request, 'data.html', {'data': [response]})

def deleteData(request):
    if request.method == 'GET':
        pk3 = request.GET.get('pk3', False)
        url= 'http://127.0.0.1:8000/api/data-delete/'+pk3
        response = requests.delete(url).json()
        return render(request, 'delSuccess.html', {'data': response})
