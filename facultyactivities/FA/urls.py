from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('admin',views.admin),
    path('admin_login',views.admin_login),
    path('details',views.admin_dashboard),
    path('faculty',views.fac_login),
    path('fac_login',views.fac_login),
    path('entry',views.fac_dashboard),
    path('detail_enter',views.detail_enter),
    path('submit_details',views.detail_enter),
    path('goback_facdash',views.goback_facdash),
    path('handle_filters',views.handle_filters)
]
