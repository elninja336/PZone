from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

# Customer table api



'''
@api_view(['GET','POST'])
def get_and_post(request):
    if request.method == 'GET':
        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)
        
@api_view(['GET','PUT','DELETE'])
def cusustomer_view(request,id):
    try:
        cust = Customer.objects.get(id = id)
    except Customer.DoesNotExist:
        return Response({'message':'Id not exists!'})
    if request.method == 'GET':
        seralizer = CustomerSerializer(cust)
        return Response(seralizer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)

        

    elif request.method == 'DELETE':
        cust.delete()
        return Response(f"Customer has been deleted")

'''


def generic_api(model_class, serializer_class):
    @api_view(['GET','POST', 'DELETE', 'PUT'])

    def api(request, id = None):
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many = True)
                return Response(serializer.data)
            
        elif request.method == 'POST':
            serializer = serializer_class(data = request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        
        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    instance.delete()
                    return Response({'message':'Delete Successfully'})
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'})
                

        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                
                        
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'})

    return api



manage_customer = generic_api(Customer, CustomerSerializer)
        
