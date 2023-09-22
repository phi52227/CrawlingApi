from rest_framework import serializers
from .models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    CultureNews,
    SportsNews,
    LifeNews
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

class SportsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsNews
        fields = "__all__"

class LifeNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeNews
        fields = "__all__"