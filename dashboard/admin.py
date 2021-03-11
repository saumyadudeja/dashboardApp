from django.contrib import admin
from .models import TicketSells,Survey

# Register your models here.
class TicketSellsAdmin(admin.ModelAdmin):
    pass
admin.site.register(TicketSells,TicketSellsAdmin)

class SurveyAdmin(admin.ModelAdmin):
    pass
admin.site.register(Survey,SurveyAdmin)
