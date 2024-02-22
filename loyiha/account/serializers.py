from .models import Account
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=68, write_only=True)
    password2 = serializers.CharField(min_length=6, max_length=68, write_only=True)

    class Meta:
        model = Account
        fields = ['id', 'name', 'email', 'img', 'password', 'password2']
        

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError({'succes': False, 'message': 'password did not match'})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        return Account.objects.create_user(**validated_data)
    