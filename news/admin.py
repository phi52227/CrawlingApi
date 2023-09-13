from django.contrib import admin
from .models import (
    PoliticsNews,
    EconomyNews,
    SocietyNews,
    LifeCultureNews,
    ItScienceNews,
)

admin.site.register(PoliticsNews)
admin.site.register(EconomyNews)
admin.site.register(SocietyNews)
admin.site.register(LifeCultureNews)
admin.site.register(ItScienceNews)
# Register your models here.
