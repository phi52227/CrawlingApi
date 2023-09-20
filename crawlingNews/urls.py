"""
URL configuration for crwalingNews project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from news.views import (
    PoliticsNewsListAPI as naverPoliticsNewsListAPI,
    EconomyNewsListAPI as naverEconomyNewsListAPI,
    SocietyNewsListAPI as naverSocietyNewsListAPI,
    LifeCultureNewsListAPI as naverLifeCultureNewsListAPI,
    ItScienceNewsListAPI as naverItScienceNewsListAPI,
)
from dongaIlbo.views import (
    PoliticsNewsListAPI as dongaIlboPoliticsNewsListAPI,
    CultureNewsListAPI as dongaIlboCultureNewsListAPI,
    EconomyNewsListAPI as dongaIlboEconomyNewsListAPI,
    InternationalNewsListAPI as dongaIlboInternationalNewsListAPI,
    EntertainmentsNewsListAPI as dongaIlboEntertainmentsNewsListAPI,
    SocietyNewsListAPI as dongaIlboSocietyNewsListAPI,
    SportsNewsListAPI as dongaIlboSportsNewsListAPI,
)

from yonhapNews.views import (
    PoliticsNewsListAPI as yonhapNewsPoliticsNewsListAPI,
    CultureNewsListAPI as yonhapNewsCultureNewsListAPI,
    EconomyNewsListAPI as yonhapNewsEconomyNewsListAPI,
    InternationalNewsListAPI as yonhapNewsInternationalNewsListAPI,
    EntertainmentsNewsListAPI as yonhapNewsEntertainmentsNewsListAPI,
    SocietyNewsListAPI as yonhapNewsSocietyNewsListAPI,
    SportsNewsListAPI as yonhapNewsSportsNewsListAPI,
    NorthKoreaNewsListAPI as yonhapNewsNorthKoreaNewsListAPI,
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/news/naver/politics", naverPoliticsNewsListAPI.as_view()),
    path("api/news/naver/economy", naverEconomyNewsListAPI.as_view()),
    path("api/news/naver/society", naverSocietyNewsListAPI.as_view()),
    path("api/news/naver/lifeculture", naverLifeCultureNewsListAPI.as_view()),
    path("api/news/naver/itscience", naverItScienceNewsListAPI.as_view()),
    path("api/news/donga/politics", dongaIlboPoliticsNewsListAPI.as_view()),
    path("api/news/donga/economy", dongaIlboEconomyNewsListAPI.as_view()),
    path("api/news/donga/society", dongaIlboSocietyNewsListAPI.as_view()),
    path("api/news/donga/culture", dongaIlboCultureNewsListAPI.as_view()),
    path("api/news/donga/international", dongaIlboInternationalNewsListAPI.as_view()),
    path("api/news/donga/entertainments", dongaIlboEntertainmentsNewsListAPI.as_view()),
    path("api/news/donga/sports", dongaIlboSportsNewsListAPI.as_view()),
    path("api/news/yonhap/politics", yonhapNewsPoliticsNewsListAPI.as_view()),
    path("api/news/yonhap/economy", yonhapNewsEconomyNewsListAPI.as_view()),
    path("api/news/yonhap/society", yonhapNewsSocietyNewsListAPI.as_view()),
    path("api/news/yonhap/culture", yonhapNewsCultureNewsListAPI.as_view()),
    path("api/news/yonhap/international", yonhapNewsInternationalNewsListAPI.as_view()),
    path("api/news/yonhap/entertainments", yonhapNewsEntertainmentsNewsListAPI.as_view()),
    path("api/news/yonhap/sports", yonhapNewsSportsNewsListAPI.as_view()),
    path("api/news/yonhap/northkorea", yonhapNewsNorthKoreaNewsListAPI.as_view()),
]
