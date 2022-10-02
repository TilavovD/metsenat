from rest_framework import serializers
from sponsor.models import Sponsor


class SponsorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('sponsor_type', 'name', 'phone_number', "total_amount", 'company')


class SponsorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'phone_number', "total_amount", 'spent_amount', 'created_at', 'status')


class SponsorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name', 'phone_number', 'total_amount', 'spent_amount', 'status')
