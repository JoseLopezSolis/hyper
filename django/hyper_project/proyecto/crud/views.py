from rest_framework import viewsets, status
from .serializers import UserSerializer
from .models import CrudUser
from handlers.response import custom_response

# Create your views here.
#En una app maximo de 4 APIS
class UserViewSet(viewsets.ViewSet):
  #GET
  def list(self, request):
    query = CrudUser.objects.all()
    serializer = UserSerializer(query, many=True)
    return custom_response("Lista de todos los usuarios", serializer.data, False, status.HTTP_200_OK)

  #POST
  def create(self, request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return custom_response("Usuario creado exitosamente", serializer.data, False, status.HTTP_200_OK)
    else: 
      return custom_response("Error al crear el usuario", serializer.errors, True, status.HTTP_400_BAD_REQUEST)

  #PUT
  def update(self, request, pk=None):
    try:
      query = CrudUser.objects.get(id=pk)
    except CrudUser.DoesNotExist:
      return custom_response("No se pudo actualizar el usuario correctamente", serializer.data, False, status.HTTP_400_BAD_REQUEST)

    data = request.data
    serializer = UserSerializer(instance = query, data = data)
    if serializer.is_valid():
      serializer.save()
      return custom_response("Usuario actualizado correctamente", serializer.data, False, status.HTTP_200_OK)
    else:
      return custom_response("No se pudo actualizar el usuario correctamente", serializer.data, False, status.HTTP_400_BAD_REQUEST)


  #DELETE
  def delete(self, request, pk=None):
    try:
      query = CrudUser.objects.get(id=pk)
    except CrudUser.DoesNotExist:
      return custom_response("No se pudo actualizar el usuario correctamente", None, False, status.HTTP_400_BAD_REQUEST)
    
    query.delete()
    return custom_response("Usuario actualizado correctamente", None, False, status.HTTP_200_OK)
    


