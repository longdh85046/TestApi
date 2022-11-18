from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import status, permissions, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from car.models import Car
from car.serializer import CarSerializer 

class ListCreateCarView(viewsets.ModelViewSet):
    model = Car
    serializer_class = CarSerializer
    # permission_classes = [permissions.IsAuthenticated]

    queryset = Car.objects.all()

    # def get_permissions(self):
    #     if self.action == 'list':  #action chi dung duoc trong viewsets
    #         return [permissions.AllowAny()]
    #     return [permissions.IsAuthenticated()] 
    
    def create(self, request, *args, **kwargs):
        queryset = Car.objects.all()
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Car successful!'
            }, status=status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)
    

class UpdateDeleteCarView(RetrieveUpdateDestroyAPIView):
    model = Car
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticated]
    def put(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data
            {
                'color': 'red'
            }
            serializer.save()
            
            return JsonResponse({
                'message': 'Update Car successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Car unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        car = get_object_or_404(Car, id=kwargs.get('pk'))
        car.delete()

        return JsonResponse({
            'message': 'Delete Car successful!'
        }, status=status.HTTP_200_OK)
