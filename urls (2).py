from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('hook/<str:endpoint>/', views.ingest_webhook, name='ingest_webhook'),
]
