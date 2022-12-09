from django.shortcuts import render
from api.models import CessaoFundo
from rest_framework import routers, serializers, viewsets

# Create your views here.
class CessaoFundoSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CessaoFundo
        fields = '__all__'


class CessaoFundoViewSet(viewsets.ModelViewSet):
    
    serializer_class = CessaoFundoSerializer
    def get_queryset(self):
        return CessaoFundo.objects.all()  



