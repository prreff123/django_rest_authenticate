from rest_framework  import serializers
from .models import *
from django.contrib.auth.models import User

class Userserial(serializers.ModelSerializer):
     class Meta:
          model = User
          fields = ['username','password']
     def create(self, validated_data):
          user = User.objects.create(username=validated_data['username'])
          user.set_password(validated_data['password'])
          user.save()
          return user     

class studentserial(serializers.ModelSerializer):
    class Meta:
        model = student
        field = ['id','name','age','father_name']
        exclude = ['roll_no']
     #    field = '_all_' 

    def validate(self, data):
            if data['age'] < 18:
                raise serializers.ValidationError({'error': "Age cannot be less than 18"})
    
            if data['name']:
                 for n in data['name']:
                      if n.isdigit():
                           raise serializers.ValidationError({'error': "Name cannot be Numeric"})                           
            return data
    
class categoryserial(serializers.ModelSerializer):
     class Meta:
          model = Category
          exclude = ['id']
          field = ['category']
          
class bookserial(serializers.ModelSerializer):
     category = categoryserial()
     class Meta:
          model = Book
          exclude = ['id']
          field = '_all_'          