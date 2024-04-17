from django.urls import path
from  .views import *
from drf import views

urlpatterns = [
     
    path('register_2/', RegisterView_2.as_view(), name='user-register'),
    path('login_2/', UserLoginView_1.as_view(), name='user-login'),
    # path('products_2/', get_products_2, name='product-list'),
    
    path('products_1/<str:token>/', ProductsView_1.as_view(), name='products'), 
    path('login123/', LoginView_1.as_view(), name='user-login'),
    path('registers/', RegisterView_1.as_view(), name='user-register'),
    
    path('employees/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', EmployeeDetailAPIView.as_view(), name='employee-detail'),
    
    
    
    # path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('products/', views.products, name='products'),
    # API URLs
    path('register1/', RegisterView.as_view(), name='api_register'),
    path('login1/', LoginView.as_view(), name='api_login'),
    path('products1/', ProductsView.as_view(), name='api_products'),
    
]
