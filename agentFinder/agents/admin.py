from django.contrib import admin
from agents.models import Agents
# Register your models here.
# class agentAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Agents)
