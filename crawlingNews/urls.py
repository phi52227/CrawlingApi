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

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/news/naver/1", naverPoliticsNewsListAPI.as_view()),
    path("api/news/naver/2", naverEconomyNewsListAPI.as_view()),
    path("api/news/naver/3", naverSocietyNewsListAPI.as_view()),
    path("api/news/naver/4", naverLifeCultureNewsListAPI.as_view()),
    path("api/news/naver/5", naverItScienceNewsListAPI.as_view()),
    path("api/news/donga/1", dongaIlboPoliticsNewsListAPI.as_view()),
    path("api/news/donga/2", dongaIlboEconomyNewsListAPI.as_view()),
    path("api/news/donga/3", dongaIlboSocietyNewsListAPI.as_view()),
    path("api/news/donga/4", dongaIlboCultureNewsListAPI.as_view()),
    path("api/news/donga/5", dongaIlboInternationalNewsListAPI.as_view()),
    path("api/news/donga/6", dongaIlboEntertainmentsNewsListAPI.as_view()),
    path("api/news/donga/7", dongaIlboSportsNewsListAPI.as_view()),
]
