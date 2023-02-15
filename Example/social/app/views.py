
from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from app.models import MyTableName
# from .serializers import MyTableNameSerializers

@api_view(['GET'])
def home(request):
    return Response("hello world")
    # items = MyTableName.objects.all()
    # serializer = MyTableNameSerializers(items,many=True)
    # return Response(serializer.data)
        

        