from django.contrib import admin
from .models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    NationwideNews,
    SocietyNews,
    CultureNews,
    ScienceNews,
    SportsNews,
    CalamityNews
)

admin.site.register(PoliticsNews)
admin.site.register(EconomyNews)
admin.site.register(InternationalNews)
admin.site.register(NationwideNews)
admin.site.register(SocietyNews)
admin.site.register(CultureNews)
admin.site.register(ScienceNews)
admin.site.register(SportsNews)
admin.site.register(CalamityNews)
# Register your models here.
