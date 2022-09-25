from rest_framework.views import APIView
from password_management_api.models import Password
from password_management_api.serializer import PasswordSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class PasswordCardList(APIView):
  
  def get(self, request):
    passwords = Password.objects.all()
    serializer = PasswordSerializer(passwords, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = PasswordSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class PasswordCardDetail(APIView):

  def get_password_card_by_pk(self, pk):
    try:
      return Password.objects.get(pk=pk)
    except Password.DoesNotExist:
      raise Http404

  def get(self, request, id):
    password = self.get_password_card_by_pk(id)
    serialiazer = PasswordSerializer(password)
    return Response(serialiazer.data)

  def put(self, request, id):
    password = self.get_password_card_by_pk(id)
    serialiazer = PasswordSerializer(password, data=request.data)
    if serialiazer.is_valid():
      serialiazer.save()
      return Response(serialiazer.data)
    return Response(serialiazer.errors, status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    password = self.get_password_card_by_pk(id)
    password.delete()
    return Response(status.HTTP_204_NO_CONTENT)

