from functools import reduce
from operator import or_
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.db.models import Q
from .models import Report


# Create your views here.

def send_data(request):
    ''' asd '''
    model = Report
    search_fields = ['id', 'name', 'description', 'start_date']

    if request.method == 'GET':
        if 'sort' in request.GET:
            sort_field = request.GET.get('sort')
        else:
            sort_field = "id"
        if 'order' in request.GET:
            if request.GET.get('order') == 'desc':
                sort_field = "-" + sort_field

        total_count = model.objects.all().count()

        if 'search' in request.GET:
            search_text = request.GET.get('search')
            q_reqiest = reduce(or_, [Q(**{'{}__contains'.format(f): search_text}) for f in search_fields],
                               Q())
            reports = model.objects.filter(q_reqiest).order_by(sort_field)
            filtered_count = reports.count()
        else:
            reports = model.objects.all().order_by(sort_field)
            filtered_count = total_count

        if 'offset' in request.GET:
            reports = reports[int(request.GET.get('offset')):]
        if 'limit' in request.GET:
            reports = reports[:int(request.GET.get('limit'))]

        serialized_queryset = {"total": filtered_count,
                               "totalNotFiltered": total_count,
                               "rows": []}
        for report in reports:
            temp = model_to_dict(report)
            temp = {k: str(v) for k, v in temp.items()}
            # пост-обработка для кнопок
            if 'link' in temp:
                links = temp['link'].split(";")
                styled_links = []
                if len(links) > 1:
                    styled_links.append('<div class="btn-group" role="group" aria-label="Basic example">')
                for link in links:
                    if "ftp://" in link:
                        styled_links.append('<a class="btn btn-warning" href="'+ link + '" role="button"> FTP</a>')
                    if "http://" in link:
                        styled_links.append('<a class="btn btn-primary" href="%s"' 
                                             'role="button"> WEB</a>' % (link))
                if len(links) > 1:
                    styled_links.append('</div>')
                temp['link'] = "\n".join(styled_links)
            serialized_queryset["rows"].append(temp)
        return JsonResponse(serialized_queryset, json_dumps_params={'indent': 2}, safe=False)
    