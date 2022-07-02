import code
from wsgiref import headers
from django.shortcuts import render
import requests
import json
from .Utilities import Snippet,Flower
def consumesnippetapi(request):
    template_name='snippetapp/apiconsume.html'
    r=  requests.get('http://127.0.0.1:8000/leela/achan')
    jsonstring=r.json()
    users_list = []   
    for u in jsonstring:    
     users_list.append(Snippet(**u))
    for item in users_list:
        print(item.title)
    return render(request,template_name,context={'r':jsonstring,'snippet':users_list})

def savesnippet(request):
    template_name='snippetapp/apipost.html'
    if request.method=='GET':        
        return render(request,template_name)
    elif request.method=='POST':
        title=request.POST.get('title')
        code=request.POST.get('code')
        style=request.POST.get('style')
        language=request.POST.get('language')
        linenos=request.POST.get('linenos')
        data={"title":title,"code":code,"style":style,"language":language,"linenos":linenos}
        headers={"Content-Type":'application/json'}
        r=  requests.post('http://127.0.0.1:8000/leela/amma/',json=data,headers=headers)
        return render(request,template_name)
def GetAllFlowers(request):
    flowerlist=[]
    template_name='snippetapp/flowerapilist.html'
    readflowers=requests.get('http://127.0.0.1:8000/leela/vava')
    myflowers=readflowers.json()
    for flowerdict in myflowers:
        flowerlist.append(Flower(**flowerdict))
    return render(request,template_name,context={'flowerlist':flowerlist})
def SaveFlower(request):
    template_name='snippetapp/flowerapisave.html'
    if request.method=="GET":
        return render(request,template_name)
        
    elif request.method=="POST":
        id=request.POST.get('id')
        flowername=request.POST.get('flowername')
        flowercolor=request.POST.get('flowercolor')
        isSingle=request.POST.get('isSingle')
        data={'id':id,'flowername':flowername,'flowercolor':flowercolor,'isSingle':isSingle}
        headers={'Content-Type':'application/json'}
        result= requests.post('http://127.0.0.1:8000/leela/abhay/',json=data,headers=headers)
        return render(request,template_name)
        
def EditFlower(request,flowerid):
    print(request.method)
    template_name="snippetapp/flowerapisave.html"
    if request.method=='GET':
        singleflower=requests.get(f'http://127.0.0.1:8000/leela/divya/{flowerid}')
        
        maani= Flower.from_json(json.dumps(singleflower.json()))
        print(json.dumps(singleflower.json()))
        context={'flower':maani}
        return render(request,template_name,context)
    elif request.method=='POST':
        print('hello bbbb')
        id=flowerid
        flowername=request.POST.get('flowername')
        flowercolor=request.POST.get('flowercolor')
        isSingle=request.POST.get('isSingle')
        data={'id':id,'flowername':flowername,'flowercolor':flowercolor,'isSingle':isSingle}
        headers={'Content-Type':'application/json'}
        result= requests.patch(f'http://127.0.0.1:8000/leela/divya/{flowerid}',json=data,headers=headers)
        return render(request,template_name)
        
            
        
