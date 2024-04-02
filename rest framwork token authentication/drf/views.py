from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import *
from datetime import datetime
from django.http import Http404




# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Product
from .serializers import ProductSerializer

# User Registration View
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import serializers, generics
from .serializers import UserSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token


# Login View
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


import requests


from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate



from rest_framework.response import Response
from rest_framework import status
import requests
# from .utils import login  # Assuming login function is in a separate module
from rest_framework.views import APIView
from rest_framework.response import Response

import requests


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView(APIView):
    
    def get_products(self,token):
        
        products = Product.objects.all()
        print("products  ", products)

        serializer = ProductSerializer(products, many=True)
        print("serializer  ", serializer)
        response_data = {
            'token': token.key,
            'user_data': serializer.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        # Extract username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')
        
        print("username, password", username, password)
        # Call the login function to authenticate the user
        
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            print("token  1==", token)
            # Call get_products method to retrieve product data
            
        if token:
            return self.get_products(token)
            # response=self.get_products(token)
            # print("response=====", response)
            # return response
            
            


    











# # Replace 'your_token_value' with the actual token value obtained during the login process
# token_value = '44551bf922642eb3b4fd08fff8d29b1f0fa9e9a6'

# # Set the URL
# url = 'http://127.0.0.1:8000/api/v1/products/'

# # Set the headers with the authorization token
# headers = {'Authorization': f'Token {token_value}'}

# # Make a GET request to the products endpoint with the token in the headers
# response = requests.get(url, headers=headers)

# # Print the response
# print('Response:', response.json())

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

def get_products(token):
        url = 'http://127.0.0.1:8000/api/v1/products/'
        headers = {'Authorization': f'Token {token}'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(data)
        else:
            # Log the error or handle it in a more appropriate way
            print(f'Error: {response.status_code} - {response.text}')



class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print("username, password", username, password)
        
        user = authenticate(username=username, password=password)

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            # get_products(token)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        

# # Protected API View
# class ProductListView(APIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)




def get_token():
    # Read the token from a file
    with open('token.txt', 'r') as file:
        return file.read().strip()

def save_token(token):
    # Save the token to a file
    with open('token.txt', 'w') as file:
        file.write(token)

# class LoginView(APIView):
#     def post(self, request):
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             token, _ = Token.objects.get_or_create(user=user)
#             save_token(token.key)  # Save the token
#             return Response({'token': token.key}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# class ProductListView(APIView):
    
#     try :
#         authentication_classes = (TokenAuthentication,)
#         permission_classes = (IsAuthenticated,)
#     except Exception as e:
#         print("error ", e)
#         def get(self, request):
#             # Retrieve the token from storage
#             token = get_token()
#             print("token=====",token)
#             products = Product.objects.all()
#             print("products  ", products)
            
#             serializer = ProductSerializer(products, many=True)
#             print("serializer  ", serializer)
            
        

#             # Include the token in the Authorization header
#             headers = {'Authorization': f'{token}'}
#             print("headers=====" ,headers)
#             # Make a GET request to the protected endpoint with the token in the headers
#             response = requests.get('http://127.0.0.1:8000/api/v1/products/', headers=headers)
#             # Print the response
#             print(response.status_code)
#             print(response.json())
#             print("response=====" ,response)
#             if response.status_code == 200:
#                 return Response(serializer.data)
#             else:
#                 return Response({'error': 'Failed to retrieve product list'}, status=status.HTTP_400_BAD_REQUEST)
            

# class ProductListView(APIView):
#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         try:
#             # Assuming you have obtained a valid token
#             token = get_token()
#             print("token=====", token)

#             # Set the headers with the Authorization token
#             headers = {'Authorization': f'Token {token}'}
#             print("headers=====", headers)

#             # Make a GET request to the protected endpoint with the token in the headers
#             response = requests.get('http://127.0.0.1:8000/api/v1/products/',headers=headers)
#             print("response======", response.text)
#             # Print the response
#             print(response.status_code)
#             # print(response.json())

#             # Retrieve the list of products
#             products = Product.objects.all()
#             print("products  ", products)

#             # Serialize the products
#             serializer = ProductSerializer(products, many=True)

#             # Return the serialized data
#             return Response(serializer.data)
#         except Exception as e:
#             print("Error:", e)
#             return Response({'error': 'Failed to retrieve product list'}, status=status.HTTP_400_BAD_REQUEST)



# class ProductListView(APIView):
#     authentication_classes = (TokenAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def get(self, request):
#         try:
#             # Retrieve the list of products
#             products = Product.objects.all()
#             print("products  ", products)
            
#             # Serialize the products
#             serializer = ProductSerializer(products, many=True)
            
#             # Return the serialized data
#             return Response(serializer.data)
#         except Exception as e:
#             print("Error:", e)
#             return Response({'error': 'Failed to retrieve product list'}, status=status.HTTP_400_BAD_REQUEST)