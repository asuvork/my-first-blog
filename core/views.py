from django.shortcuts import render
from django.urls import reverse
from collections import OrderedDict
from .models import ReportKind, ReportType, InfoKind, InfoType, device
from django.conf import settings
from functools import reduce
from operator import or_
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q


def get_mr():
    """Get MR name according to IP in settings.ALLOWED_HOSTS"""
    mr_dict = {"10.233.204.55": ["Дальний Восток", "ДВ"],
               "10.233.204.47": ["Сибирь", "СИБ"],
               "10.233.204.48": ["Урал", "УРЛ"],
               "10.233.204.56": ["Центр", "ЦНТ"],
               "10.233.204.53": ["Северо-Запад", "СЗ"],
               "10.233.204.51": ["Москва", "МСК"]
              }
    for mr_ip in mr_dict:
        if mr_ip in settings.ALLOWED_HOSTS:
            return mr_dict[mr_ip]
    return ["Неизвестный МР", "МР?"]


def get_vendor_menu():
    menu_reports = {}
    for report_kind in ReportKind.objects.all():
        print(report_kind)
        report_types = ReportType.objects.filter(report_kind=report_kind)
        if report_types.count() > 0:
            menu_reports[report_kind] = []
            for report_type in report_types:
                menu_reports[report_kind].append(report_type)
    print(menu_reports)
    menu_info = {}
    for info_kind in InfoKind.objects.all():
        info_types = InfoType.objects.filter(info_kind=info_kind)
        if info_types.count() > 0:
            menu_info[info_kind] = []
            for info_type in info_types:
                menu_info[info_kind].append(info_type)
    print(menu_info)
    return menu_reports, menu_info


# Create your views here.
def vendor(request):
    mr = get_mr()
    menu_reports, menu_info = get_vendor_menu()
    return render(request, 'core/vendor.html', {'mr': mr,
                                                'menu_reports': menu_reports,
                                                'menu_info': menu_info})


def mbh_json(request):
    """ Get Device list as json """
    model = device
    search_fields = ['region', 'hostname', 'address']

    if request.method == 'GET':
        if 'sort' in request.GET:
            sort_field = request.GET.get('sort')
        else:
            sort_field = search_fields[0]
        if 'order' in request.GET:
            if request.GET.get('order') == 'desc':
                sort_field = "-" + sort_field

        total_count = model.objects.all().count()

        if 'search' in request.GET:
            search_text = request.GET.get('search')
            q_request = reduce(or_, [Q(**{'{}__contains'.format(f): search_text}) for f in search_fields],
                               Q())
            records = model.objects.filter(q_request).order_by(sort_field)
            filtered_count = records.count()
        else:
            records = model.objects.all().order_by(sort_field)
            filtered_count = total_count

        if 'offset' in request.GET:
            records = records[int(request.GET.get('offset')):]
        if 'limit' in request.GET:
            records = records[:int(request.GET.get('limit'))]

        serialized_queryset = {"total": filtered_count,
                               "totalNotFiltered": total_count,
                               "rows": []}
        for report in records:
            temp = model_to_dict(report)

            # пост-обработка
            temp["asnum"] = ' '.join(map(str, temp["asnum"]))  # для получения asnum в виде строки
            temp["address"] = '<a href="' + reverse('mbh_deviсe', kwargs={"address": temp["address"]}) + '">' + temp["address"] + '</a>'
            #temp = {k: str(v) for k, v in temp.items()}

            serialized_queryset["rows"].append(temp)
        return JsonResponse(serialized_queryset, json_dumps_params={'indent': 2}, safe=False)


def mbh_nodes(request):
    """ Table with all devices """
    mr = get_mr()
    menu_reports, menu_info = get_vendor_menu()
    data_source = reverse('mbh_json')  # из urls.py
    columns = {"region": "Регион", 
               "regionid": "RegID", 
               "address": "Aдрес",
               "hostname": "Узел",
               "asnum": "AS",
               "modeltype": "Модель",
               "softver": "ПО",
               "igp_routes": "IGP",
               "vpnv4_routes": "VPNv4"}

    columns = OrderedDict([
        ("region", "Регион"), 
        ("regionid", "RegID"), 
        ("address", "Aдрес"), 
        ("hostname", "Узел"), 
        ("asnum", "AS"), 
        ("modeltype", "Модель"), 
        ("softver", "ПО"), 
        ("igp_routes", "IGP"), 
        ("vpnv4_routes", "VPNv4")
    ])

    return render(request, 'core/device_list.html', {'mr': mr,
                                                     'menu_reports': menu_reports,
                                                     'menu_info': menu_info,
                                                     'data_source': data_source,
                                                     'columns': columns})


def report(request, report_kind, report_type):
    pass


def info(request, report_kind, report_type):
    pass


def device1(request, address):
    pass
