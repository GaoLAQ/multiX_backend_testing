from rest_framework import serializers
from .models import MaterialCard

class MaterialCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialCard
        fields = ('id','title', 'uploadImage', 'description', 'anisotropic', 'materialType' )  