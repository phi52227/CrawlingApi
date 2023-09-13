from rest_framework import serializers
from .models import (
    PoliticsNews,
    EconomyNews,
    SocietyNews,
    LifeCultureNews,
    ItScienceNews,
)


class PoliticsNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoliticsNews
        fields = "__all__"


class EconomyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomyNews
        fields = "__all__"


class SocietyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocietyNews
        fields = "__all__"


class LifeCultureNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LifeCultureNews
        fields = "__all__"


class ItScienceNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItScienceNews
        fields = "__all__"
