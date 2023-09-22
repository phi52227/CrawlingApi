from django.contrib import admin
from .models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    CultureNews,
    SportsNews,
    LifeNews
)

admin.site.register(PoliticsNews)
admin.site.register(EconomyNews)
admin.site.register(InternationalNews)
admin.site.register(SocietyNews)
admin.site.register(CultureNews)
admin.site.register(SportsNews)
admin.site.register(LifeNews)
# Register your models here.
