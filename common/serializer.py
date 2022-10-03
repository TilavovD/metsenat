from rest_framework import serializers
from .models import StudentSponsor
from student.models import Student
from sponsor.models import Sponsor


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name',)


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('name',)


class StudentSponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentSponsor
        fields = "__all__"

    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['student'].total_contract == data['student'].received_amount:
            raise serializers.ValidationError(
                {"price": "Ushbu talaba kontrakt summasiga teng miqdordagi summani allaqachon qabul qilib olgan"}
            )
        elif data['student'].total_contract - data['student'].received_amount < data['amount']:
            raise serializers.ValidationError(
                {"price": "Talabaga ajratilayotgan summa uning kontrakt summasidan katta bo'la olmaydi"})

        elif data['sponsor'].total_amount - data['sponsor'].spent_amount < data['amount']:
            raise serializers.ValidationError(
                {"price": f"Talabaga ajratilayotgan summa homiy balansida qolgan puldan katta bo'la olmaydi. "
                          f"\nMaksimum ajratish mumkin bo'lgan summa "
                          f"{data['sponsor'].total_amount - data['sponsor'].spent_amount} so'm"})

        return data


class StudentSponsorListSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    sponsor = SponsorSerializer()

    class Meta:
        model = StudentSponsor
        fields = ("student", "sponsor", 'amount',)
        depth = 1
