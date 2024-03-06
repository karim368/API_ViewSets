from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from app.serializers import *

class ProductCrud(ViewSet):
    def list(self,request):
        po = Product.objects.all()
        jsonobj = ProductModelSerializer(po,many=True)
        return Response(jsonobj.data)
    
    def retrieve(self,request,pk):
        po = Product.objects.get(product_id=pk)
        jsonobj = ProductModelSerializer(po)
        return Response(jsonobj.data)
    
    def create(self,request):
        jsonobj = request.data
        jsondata = ProductModelSerializer(data=jsonobj)
        if jsondata.is_valid():
            jsondata.save()
            return Response({'insert':'Data is inserted'})
        else:
            return Response({'error':'data is not inserted'})
        
    def update(self,request,pk):
        po = Product.objects.get(product_id=pk)
        ormdata = ProductModelSerializer(po,data=request.data)
        
        if ormdata.is_valid():
            ormdata.save()
            return Response({'update':'Data is updated'})
        else:
            return Response({'error':'Data is not updated'})
        
    def partial_update(self,request,pk):
        po = Product.objects.get(product_id=pk)
        ormdata = ProductModelSerializer(po,data=request.data,partial=True)
        if ormdata.is_valid():
            ormdata.save()
            return Response({'update':'Data is updated'})
        else:
            return Response({'error':'Data is not updated'})
        
    def destroy(self,request,pk):
        Product.objects.get(product_id=pk).delete()
        return Response({'delete':'Data is deleted'})
        