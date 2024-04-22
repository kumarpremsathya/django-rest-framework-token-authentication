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

from django.http import HttpRequest 


from rest_framework.response import Response
from rest_framework import status
import requests
# from .utils import login  # Assuming login function is in a separate module
from rest_framework.views import APIView
from rest_framework.response import Response

import requests
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics, permissions


# Django Views
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .models import Product
from .serializers import UserSerializer, ProductSerializer


#DRF Tokem Authentication with frontend application

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class LoginView(APIView):
    def post(self, request):
        # Extract username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')
        print("username,password====:", username,password)
        # Authenticate the user
        user = authenticate(username=username, password=password)
        if user:
            # Generate token
            token, _ = Token.objects.get_or_create(user=user)
            # Debug statement
            print("Token:", token.key)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # Return error response if authentication fails
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ProductsView(LoginView):
    
    def get(self, request):
        # Get the token from the request headers
        token = request.headers.get('Authorization')

        # Ensure the token is valid
        try:
            token_obj = Token.objects.get(key=token)
            print('token_obj===', token_obj)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Retrieve product data
        # products = Product.objects.all()
        # serializer = ProductSerializer(products, many=True)
        # response_data = {
        #     'token': token,
        #     'user_data': serializer.data,   
        # }
        
        # print('response_data===', response_data)
        
        
        # Retrieve product data for the authenticated user
        products = Product.objects.filter(user=token_obj.user)
        serializer = ProductSerializer(products, many=True)
        response_data = {
            'token': token,
            'user_data': serializer.data,
        }
        print('response_data===', response_data)
        
        # Render the products.html template with the response data
        # return render(request, 'products.html', context=response_data)
        
        return Response(response_data, status=status.HTTP_200_OK)



        
class CreateProductView(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)




    
    

def register(request):
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def products(request):
    return render(request, 'products.html')


def create_product(request):
    return render(request, 'create_product.html')








###########################################################################################################




# #function for showing results in same UserLoginView(APIView) class

class RegisterView_2(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserLoginView_1(APIView):
    
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
        else:
            # Return error response if authentication fails
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)  
            


    
    

    
    
    
    

#function for showing results in  ProductsView(APIView) class after user logged in UserLoginView(APIView) class


class RegisterView_1(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductsView_1(APIView):
    def get(self, request, token):
        # Ensure the token is valid
        try:
            token_obj = Token.objects.get(key=token)
            print('token_obj===' , token_obj)
        except Token.DoesNotExist:
            return Response({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)
        
        # Retrieve product data
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        response_data = {
            'token': token,
            'user_data': serializer.data,   
        }
        return Response(response_data, status=status.HTTP_200_OK)

class LoginView_1(APIView):
    def post(self, request):
        # Extract username and password from request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user:
            # Generate token
            token, _ = Token.objects.get_or_create(user=user)
            # Debug statement
            print("Token:", token.key)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
            
        else:
            # Return error response if authentication fails
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)





class EmployeeListAPIView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return None

    def get(self, request, pk):
        employee = self.get_object(pk)
        if employee:
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)
        else:
            return Response({"result":"no data"}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        employee = self.get_object(pk)
        if employee:
            serializer = EmployeeSerializer(employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, pk):
        employee = self.get_object(pk)
        if employee:
            serializer = EmployeeSerializer(employee, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        employee = self.get_object(pk)
        if employee:
            employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)




##########################################################################################################


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