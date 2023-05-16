from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.dView,name= "home"),
    path('add_product',views.add_product,name='add_product'),
    
    
    path('category/',views.getCategory),
    path('product/',views.getProducts),
    path('create_category/',views.postCategory),
    path('create_product/',views.postProducts),
    path('category/<str:pk>/',views.getCategoryById),
    path('product/<str:pk>/',views.getProductsById),
    path('update_category/<str:pk>/',views.updateCategory),
    path('update_product/<str:pk>/',views.updateProducts),
    path('delete_category/<str:pk>/',views.DeleteCategory.as_view()),
    path('delete_product/<str:pk>/',views.DeleteProduct.as_view()),
]
