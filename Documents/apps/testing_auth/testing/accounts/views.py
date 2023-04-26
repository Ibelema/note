from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import SignUpSerializer
from rest_framework.views import APIView
from django.contrib.auth import authenticate
# Create your views here.

@api_view(['POST'])
def signuppage(request:Request):
    
        

        
    if request.method == 'POST':
        data = request.data
        serializer = SignUpSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'user created successfully', 'data':serializer.data}
            return Response(data=response, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginView(APIView):

    def post(self,request:Request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            response = {
                'message':'login successful',
                'token': user.authtoken.key
            }
            return Response(data=response, status=status.HTTP_200_OK)

        else:
            return Response(data={'message': 'invalid login details'})

            
    def get(self, request:Request):
        content = {
            'user':str(request.user),
            'auth':str(request.auth)
        }

        return Response(data=content, status=status.HTTP_200_OK)
   # return Response(data=serializer.data, status=status.HTTP_200_OK)

 #  {"email":"johndoe@app.com",
  #  "username": "johndoe",
   # "password":"password"
    #}