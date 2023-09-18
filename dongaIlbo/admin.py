from django.contrib import admin
from .models import (
    PoliticsNews,
    EconomyNews,
    InternationalNews,
    SocietyNews,
    CultureNews,
    EntertainmentsNews,
    SportsNews,
)

admin.site.register(PoliticsNews)
admin.site.register(EconomyNews)
admin.site.register(InternationalNews)
admin.site.register(SocietyNews)
admin.site.register(CultureNews)
admin.site.register(EntertainmentsNews)
admin.site.register(SportsNews)
# Register your models here.
