from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CategoryModel, ProductsModel

from .serializer import CategorySerializer, ProductSerializer


def add_product(request):
    cats=CategoryModel.objects.all()       
    if request.method == "POST":
        data = request.POST
        imo = request.FILES.getlist ('image') 
        category = CategoryModel.objects.get(id=data['category'])
        for i in imo:
            ProductsModel.objects.get_or_create(
                name = data['name'],
                image = i,
                category = category,
                price = data['price'],
                desc = data['desc'],
                
            )
        return redirect('home')
    return render(request,'base/add_product.html',{'cats':cats})


def dView(request):
    product = ProductsModel.objects.all()
    cats = CategoryModel.objects.all()
    return render (request, 'base/home.html',{
        'product':product,
        'cats':cats,
    })
#----------------------------------------

@api_view(['GET'])
def getCategoryById(request, pk):
    data = CategoryModel.objects.get(id=pk)
    serializer= CategorySerializer(data, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getProductsById(request, pk):
    data = ProductsModel.objects.get(id=pk)
    serializer= ProductSerializer(data, many=False)
    print(serializer)
    return Response(serializer.data)





#---------------------------------------

@api_view(['GET'])
def getCategory(request):
    data = CategoryModel.objects.all()
    serializer= CategorySerializer(data, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProducts(request):
    data = ProductsModel.objects.all()
    
    serializer= ProductSerializer(data, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def postCategory(request):
    data = request.data
    post = CategoryModel.objects.create(
        name=data['name'],
    )
    serializer= CategorySerializer(post, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def postProducts(request):
    data = request.data
    
    post = ProductsModel.objects.create(
        name=data["name"],
        image=request.FILES.get('image'),
        price = data['price'],
        desc = data['desc'],
        category = CategoryModel.objects.get(name=data['category']),
        
    )
    serializer= ProductSerializer(post, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
def updateCategory(request,pk):
    data = request.data
    post = CategoryModel.objects.get(id=pk)
    serializer= CategorySerializer(post, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['PUT'])
def updateProducts(request, pk):
    data = request.data
    post = ProductsModel.objects.get(id=pk)
    print(post)
    serializer= ProductSerializer(post, data=request.data,partial=True)
    print(serializer)    
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteCategory(request,pk):
    data = CategoryModel.objects.get(id=pk)
    data.delete()
    return Response('Its Deleted !')


@api_view(['DELETE'])
def deleteProducts(request, pk):
    data = ProductsModel.objects.get(id=pk)
    data.delete()
    return Response('Its Deleted !')



