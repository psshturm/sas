from django.conf import settings
from django.urls import path

from . import views

urlpatterns = [
    path('', views.CounterpartiesList.as_view(), name='counterparties_list'),
    path('tune_up/', views.TuneUpList.as_view(), name='tune_up_list'),
    path('<pk>/', views.CounterpartyDetail.as_view(), name='detail_counterparty'),
    
]
