from django.db import models
from datetime import date

# Create your models here.
class ReportKind(models.Model):
    label = models.CharField(max_length=50, null=True, blank=True)
    url_name = models.CharField(max_length=1000, null=True, blank=True)
    icon = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.label

    def __str__(self):
        return self.label


class ReportType(models.Model):
    label = models.CharField(max_length=1000, null=True, blank=True, unique=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    url_name = models.CharField(max_length=1000, null=True, blank=True)
    crtime = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    vendor = models.CharField(max_length=50, null=True, blank=True)
    kind = models.CharField(max_length=50, null=True, blank=True)
    report_kind = models.ForeignKey(ReportKind, on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        return self.label

    def __str__(self):
        return self.label


class InfoKind(models.Model):
    label = models.CharField(max_length=50, null=True, blank=True)
    url_name = models.CharField(max_length=1000, null=True, blank=True)
    icon = models.CharField(max_length=50, null=True, blank=True)

    def __unicode__(self):
        return self.label

    def __str__(self):
        return self.label


class InfoType(models.Model):
    label = models.CharField(max_length=1000, null=True, blank=True, unique=True)
    url = models.CharField(max_length=1000, null=True, blank=True)
    url_name = models.CharField(max_length=1000, null=True, blank=True)
    crtime = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    vendor = models.CharField(max_length=50, null=True, blank=True)
    into_kind = models.ForeignKey(InfoKind, on_delete=models.CASCADE, null=True, blank=True)

    def __unicode__(self):
        return self.label

    def __str__(self):
        return self.label


class ASnum(models.Model):
    asnum = models.CharField(max_length=1000, null=True, blank=True, unique=True)
    region = models.CharField(max_length=1000, null=True, blank=True)
    regionid = models.CharField(max_length=200, null=True, blank=True)
    regionname = models.CharField(max_length=1000, null=True, blank=True)
    astype = models.CharField(max_length=20, null=True, blank=True)

    def __unicode__(self):
        return self.asnum or u'None'

    def __str__(self):
        return self.asnum


class device(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, unique=True) # Name from NSO
    hostname = models.CharField(max_length=200, null=True, blank=True, unique=False)
    address = models.CharField(max_length=200, null=True, blank=True)
    region = models.CharField(max_length=200, null=True, blank=True)
    regionid = models.CharField(max_length=200, null=True, blank=True)
    mr = models.CharField(max_length=200, null=True, blank=True)
    modeltype = models.CharField(max_length=200, null=True, blank=True)
    softver = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.CharField(max_length=200, null=True, blank=True) # SHIROTA
    longitude = models.CharField(max_length=200, null=True, blank=True) # DOLGOTA
    pub_date = models.DateField(default=date.today, null=True, blank=True)
    igp_routes = models.PositiveIntegerField(null=True, blank=True)
    vpnv4_routes = models.PositiveIntegerField(null=True, blank=True)

    asnum = models.ManyToManyField(ASnum)

    def __unicode__(self):
        return self.name or u'None'

    def __str__(self):
        return self.name
