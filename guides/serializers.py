from rest_framework import serializers
from .models import guide

class GuidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = guide
        fields =  "__all__"
    
