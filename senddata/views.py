from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Report
import json


# Create your views here.

def send_data(request):
    reports = Report.objects.all().order_by('start_date')
    serialized_queryset = {"total": reports.count(),
                           "totalNotFiltered": reports.count(),
                           "rows": []}
    for report in reports:
        temp = model_to_dict(report)
        #temp = {k: str(v) for k, v in temp.items()}
        serialized_queryset["rows"].append(temp)
        
    #serialized_queryset = serialize_bootstraptable(Report.objects.all())
    return JsonResponse(serialized_queryset, json_dumps_params={'indent': 2}, safe=False)
    


def serialize_bootstraptable(queryset):
    json_data = serialize('json', queryset)
    json_final = {"total": queryset.count(), "rows": []}
    data = json.loads(json_data)
    for item in data:
        del item["model"]
        item["fields"].update({"id": item["pk"]})
        item = item["fields"]
        json_final['rows'].append(item)
    return json_final
