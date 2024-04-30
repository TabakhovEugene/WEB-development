from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bug_page_url = reverse('quality_control:bug_list')
    feature_page_url = reverse('quality_control:feature_list')
    html = (f"<h1>Система контроля качеств</h1>"
            f"<a href='{bug_page_url}'>Список всех багов</a> "
            f"<a href='{feature_page_url}'>Запросы на улучшениe</a>"
    )
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse("Cписок отчетов об ошибках")

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def bug_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")
