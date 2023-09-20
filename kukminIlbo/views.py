from django.shortcuts import render
from rest_framework.response import Response
from .models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    IssueNews,
    EntertainmentsNews,
    SportsNews,
    LifeNews
)
from rest_framework.views import APIView
from .serializers import (
    PoliticsNewsSerializer,
    EconomyNewsSerializer,
    SocietyNewsSerializer,
    InternationalNewsSerializer,
    IssueNewsSerializer,
    EntertainmentsNewsSerializer,
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


class IssueNewsListAPI(APIView):
    def get(self, request):
        queryset = IssueNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = IssueNewsSerializer(queryset, many=True)
        return Response(serializers.data)


class EntertainmentsNewsListAPI(APIView):
    def get(self, request):
        queryset = EntertainmentsNews.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = EntertainmentsNewsSerializer(queryset, many=True)
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

# Create your views here.
