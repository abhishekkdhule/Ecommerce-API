from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.views import APIView
from users.serializer import SigninSerializer, SignupSerializer
from rest_framework import status
# @api_view(['GET'])
# def signup(request):
#     return Response({}, status=200)


# @api_view(['GET'])
# def signin(request):
#     return Response(status=200)


class Signup(APIView):
    """
    User registeration API
    """
    def post(self, request, format=None):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(kwargs={"user_type": "customer"})
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SigninView(APIView):
    """
    """

    def post(self, request):
        serializer = SigninSerializer(data=request.data)
        if serializer.is_valid():
            access_token = serializer.validated_data.get('access_token')
            headers = {
                'Authorization': f'Bearer ${access_token}',
            }
            return Response(data=serializer.validated_data, status=status.HTTP_200_OK, headers=headers)
