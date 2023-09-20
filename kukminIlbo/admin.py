from django.contrib import admin
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

admin.site.register(PoliticsNews)
admin.site.register(EconomyNews)
admin.site.register(InternationalNews)
admin.site.register(SocietyNews)
admin.site.register(IssueNews)
admin.site.register(EntertainmentsNews)
admin.site.register(SportsNews)
admin.site.register(LifeNews)
# Register your models here.
