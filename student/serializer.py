from rest_framework import serializers
from .models import Student, University


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'phone_number', "total_contract", 'university', 'degree')


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'degree', 'university', 'total_contract', 'received_amount')


class StudentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 'phone_number', "total_contract", 'university', 'degree')


class CreateUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('name',)
