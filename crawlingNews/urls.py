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

from kukminIlbo.views import (
    PoliticsNewsListAPI as kukminIlboPoliticsNewsListAPI,
    IssueNewsListAPI as kukminIlboIssueNewsListAPI,
    EconomyNewsListAPI as kukminIlboEconomyNewsListAPI,
    InternationalNewsListAPI as kukminIlboInternationalNewsListAPI,
    EntertainmentsNewsListAPI as kukminIlboEntertainmentsNewsListAPI,
    SocietyNewsListAPI as kukminIlboSocietyNewsListAPI,
    SportsNewsListAPI as kukminIlboSportsNewsListAPI,
    LifeNewsListAPI as kukminIlboLifeNewsListAPI,
)
from ytnNews.views import (
    PoliticsNewsListAPI as ytnNewsPoliticsNewsListAPI,
    EconomyNewsListAPI as ytnNewsEconomyNewsListAPI,
    InternationalNewsListAPI as ytnNewsInternationalNewsListAPI,
    NationwideNewsListAPI as ytnNewsNationwideNewsListAPI,
    SocietyNewsListAPI as ytnNewsSocietyNewsListAPI,
    CultureNewsListAPI as ytnNewsCultureNewsListAPI,
    ScienceNewsListAPI as ytnNewsScienceNewsListAPI,
    SportsNewsListAPI as ytnNewsSportsNewsListAPI,
    CalamityNewsListAPI as ytnNewsCalamityNewsListAPI
)
from joongangIlbo.views import (
    PoliticsNewsListAPI as joongangNewsPoliticsNewsListAPI,
    EconomyNewsListAPI as joongangNewsEconomyNewsListAPI,
    InternationalNewsListAPI as joongangNewsInternationalNewsListAPI,
    SocietyNewsListAPI as joongangNewsSocietyNewsListAPI,
    CultureNewsListAPI as joongangNewsCultureNewsListAPI,
    SportsNewsListAPI as joongangNewsSportsNewsListAPI,
    LifeNewsListAPI as joongangNewsLifeNewsListAPI
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # naver
    path("api/news/naver/politics", naverPoliticsNewsListAPI.as_view()),
    path("api/news/naver/economy", naverEconomyNewsListAPI.as_view()),
    path("api/news/naver/society", naverSocietyNewsListAPI.as_view()),
    path("api/news/naver/lifeculture", naverLifeCultureNewsListAPI.as_view()),
    path("api/news/naver/itscience", naverItScienceNewsListAPI.as_view()),
    # donga
    path("api/news/donga/politics", dongaIlboPoliticsNewsListAPI.as_view()),
    path("api/news/donga/economy", dongaIlboEconomyNewsListAPI.as_view()),
    path("api/news/donga/society", dongaIlboSocietyNewsListAPI.as_view()),
    path("api/news/donga/culture", dongaIlboCultureNewsListAPI.as_view()),
    path("api/news/donga/international", dongaIlboInternationalNewsListAPI.as_view()),
    path("api/news/donga/entertainments", dongaIlboEntertainmentsNewsListAPI.as_view()),
    path("api/news/donga/sports", dongaIlboSportsNewsListAPI.as_view()),
    # yonhap
    path("api/news/yonhap/politics", yonhapNewsPoliticsNewsListAPI.as_view()),
    path("api/news/yonhap/economy", yonhapNewsEconomyNewsListAPI.as_view()),
    path("api/news/yonhap/society", yonhapNewsSocietyNewsListAPI.as_view()),
    path("api/news/yonhap/culture", yonhapNewsCultureNewsListAPI.as_view()),
    path("api/news/yonhap/international", yonhapNewsInternationalNewsListAPI.as_view()),
    path("api/news/yonhap/entertainments", yonhapNewsEntertainmentsNewsListAPI.as_view()),
    path("api/news/yonhap/sports", yonhapNewsSportsNewsListAPI.as_view()),
    path("api/news/yonhap/northkorea", yonhapNewsNorthKoreaNewsListAPI.as_view()),
    # kukmin
    path("api/news/kukmin/politics", kukminIlboPoliticsNewsListAPI.as_view()),
    path("api/news/kukmin/economy", kukminIlboEconomyNewsListAPI.as_view()),
    path("api/news/kukmin/society", kukminIlboSocietyNewsListAPI.as_view()),
    path("api/news/kukmin/issue", kukminIlboIssueNewsListAPI.as_view()),
    path("api/news/kukmin/international", kukminIlboInternationalNewsListAPI.as_view()),
    path("api/news/kukmin/entertainments", kukminIlboEntertainmentsNewsListAPI.as_view()),
    path("api/news/kukmin/sports", kukminIlboSportsNewsListAPI.as_view()),
    path("api/news/kukmin/life", kukminIlboLifeNewsListAPI.as_view()),
    # ytn
    path("api/news/ytn/politics", ytnNewsPoliticsNewsListAPI.as_view()),
    path("api/news/ytn/economy", ytnNewsEconomyNewsListAPI.as_view()),
    path("api/news/ytn/society", ytnNewsSocietyNewsListAPI.as_view()),
    path("api/news/ytn/nationwide", ytnNewsNationwideNewsListAPI.as_view()),
    path("api/news/ytn/international", ytnNewsInternationalNewsListAPI.as_view()),
    path("api/news/ytn/culture", ytnNewsCultureNewsListAPI.as_view()),
    path("api/news/ytn/sports", ytnNewsSportsNewsListAPI.as_view()),
    path("api/news/ytn/science", ytnNewsScienceNewsListAPI.as_view()),
    path("api/news/ytn/calamity", ytnNewsCalamityNewsListAPI.as_view()),
    # joongang
    path("api/news/joongang/politics", joongangNewsPoliticsNewsListAPI.as_view()),
    path("api/news/joongang/economy", joongangNewsEconomyNewsListAPI.as_view()),
    path("api/news/joongang/society", joongangNewsSocietyNewsListAPI.as_view()),
    path("api/news/joongang/international", joongangNewsInternationalNewsListAPI.as_view()),
    path("api/news/joongang/culture", joongangNewsCultureNewsListAPI.as_view()),
    path("api/news/joongang/sports", joongangNewsSportsNewsListAPI.as_view()),
    path("api/news/joongang/life", joongangNewsLifeNewsListAPI.as_view()),
]
