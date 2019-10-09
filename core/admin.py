from django.contrib import admin
from .models import ReportKind, ReportType, InfoKind, InfoType, device, ASnum

# Register your models here.
admin.site.register(ReportKind)
admin.site.register(ReportType)
admin.site.register(InfoKind)
admin.site.register(InfoType)
admin.site.register(device)
admin.site.register(ASnum)