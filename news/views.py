from django.shortcuts import render
from rest_framework.response import Response
from .models import (
    PoliticsNews,
    EconomyNews,
    SocietyNews,
    LifeCultureNews,
    ItScienceNews,
)
from rest_framework.views import APIView
from .serializers import (
    PoliticsNewsSerializer,
    EconomyNewsSerializer,
    SocietyNewsSerializer,
    LifeCultureNewsSerializer,
    ItScienceNewsSerializer,
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


class SocietyNewsListAPI(APIView):
    def get(self, request):
        queryset = SocietyNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = SocietyNewsSerializer(queryset, many=True)
        return Response(serializers.data)


class LifeCultureNewsListAPI(APIView):
    def get(self, request):
        queryset = LifeCultureNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = LifeCultureNewsSerializer(queryset, many=True)
        return Response(serializers.data)


class ItScienceNewsListAPI(APIView):
    def get(self, request):
        queryset = ItScienceNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = ItScienceNewsSerializer(queryset, many=True)
        return Response(serializers.data)


# Create your views here.
