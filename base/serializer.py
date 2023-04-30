from rest_framework.serializers import ModelSerializer
from .models import CategoryModel, ProductsModel



class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields= '__all__'



class ProductSerializer(ModelSerializer): 
    class Meta:
        model= ProductsModel
        fields = '__all__'   