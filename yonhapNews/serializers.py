from rest_framework import serializers
from .models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    CultureNews,
    EntertainmentsNews,
    SportsNews,
    NorthKoreaNews
)


class PoliticsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticsNews
        fields = "__all__"


class EconomyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomyNews
        fields = "__all__"


class InternationalNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternationalNews
        fields = "__all__"


class SocietyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyNews
        fields = "__all__"


class CultureNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureNews
        fields = "__all__"


class EntertainmentsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntertainmentsNews
        fields = "__all__"


class SportsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsNews
        fields = "__all__"

class NorthKoreaNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NorthKoreaNews
        fields = "__all__"