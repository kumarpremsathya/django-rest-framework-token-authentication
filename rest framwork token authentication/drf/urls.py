from django.urls import path
from  .views import *

urlpatterns = [
     
    
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('products/', get_products, name='product-list'),
    # Optionally, you can define a registration endpoint if needed
    # path('register/', UserRegistrationView.as_view(), name='user-register'),
    
    path('register/', RegisterView.as_view(), name='user-register'),
    #  path('login/', LoginView.as_view(), name='user-login'),
    # path('products/', ProductListView.as_view(), name='product-list'),
     

]
