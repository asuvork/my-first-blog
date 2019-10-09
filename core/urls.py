from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor, name='vendor'),
    path('mbh/', views.mbh_nodes, name='mbh'),
    path('mbh/json', views.mbh_json, name='mbh_json'),
    path('mbh/device/<str:address>/', views.device1, name='mbh_deviсe'),
    path('repоrts/', views.vendor, name='reports'),
    path('report/<str:report_kind>/<str:report_type>/', views.report, name='report'),
    path('info/<str:info_kind>/<str:info_type>/', views.info, name='info'),
]
