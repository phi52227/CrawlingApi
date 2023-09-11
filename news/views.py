from django.shortcuts import render
from rest_framework.response import Response
from .models import News
from rest_framework.views import APIView
from .serializers import NewsSerializer


class NewsListAPI(APIView):
    def get(self, request):
        queryset = News.objects.all().order_by("-order")[:40]
        # print(queryset)
        serializers = NewsSerializer(queryset, many=True)
        return Response(serializers.data)


# Create your views here.
