from django.urls import path
from  .views import *

urlpatterns = [
     
    
    path('login/', UserLoginView.as_view(), name='user-login'),
    # path('products/', get_products, name='product-list'),
    path('products/<str:token>/', ProductsView.as_view(), name='products'),
    
    path('login2/', LoginView.as_view(), name='user-login'),
    path('register/', RegisterView.as_view(), name='user-register'),
    
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
    
]
