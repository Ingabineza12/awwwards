from rest_framework import serializers
from .models import Project,Profile

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title', 'description', 'link','image')

class MerchSerializerProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('profile_pic', 'bio', 'contact')
