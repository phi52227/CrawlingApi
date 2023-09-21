from rest_framework import serializers
from .models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    NationwideNews,
    SocietyNews,
    CultureNews,
    ScienceNews,
    SportsNews,
    CalamityNews
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
        
class ScienceNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScienceNews
        fields = "__all__"


class CultureNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CultureNews
        fields = "__all__"


class NationwideNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NationwideNews
        fields = "__all__"


class SportsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SportsNews
        fields = "__all__"

class CalamityNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalamityNews
        fields = "__all__"