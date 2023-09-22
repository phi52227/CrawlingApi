from django.shortcuts import render

from .models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    CultureNews,
    SportsNews,
    LifeNews
)
from rest_framework.views import APIView
from .serializers import (
    PoliticsNewsSerializer,
    EconomyNewsSerializer,
    SocietyNewsSerializer,
    InternationalNewsSerializer,
    CultureNewsSerializer,
    SportsNewsSerializer,
    LifeNewsSerializer
)


class PoliticsNewsListAPI(APIView):
    def get(self, request):
        queryset = PoliticsNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = PoliticsNewsSerializer(queryset, many=True)
        return Response(serializers.data)


class EconomyNewsListAPI(APIView):
    def get(self, request):
        queryset = EconomyNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = EconomyNewsSerializer(queryset, many=True)
        return Response(serializers.data)


class InternationalNewsListAPI(APIView):
    def get(self, request):
        queryset = InternationalNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = InternationalNewsSerializer(queryset, many=True)
        return Response(serializers.data)

class SocietyNewsListAPI(APIView):
    def get(self, request):
        queryset = SocietyNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = SocietyNewsSerializer(queryset, many=True)
        return Response(serializers.data)


class CultureNewsListAPI(APIView):
    def get(self, request):
        queryset = CultureNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = CultureNewsSerializer(queryset, many=True)
        return Response(serializers.data)


class SportsNewsListAPI(APIView):
    def get(self, request):
        queryset = SportsNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = SportsNewsSerializer(queryset, many=True)
        return Response(serializers.data)

class LifeNewsListAPI(APIView):
    def get(self, request):
        queryset = LifeNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = LifeNewsSerializer(queryset, many=True)
        return Response(serializers.data)
