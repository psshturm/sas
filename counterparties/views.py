from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from .models import Counterparties, SparkSettings, NotificationSettings, SourceSettings, News

# Create your views here.
class CounterpartiesList(TemplateView):
    template_name = 'counterparties/counterparties_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['c_list'] = Counterparties.objects.all().order_by('-с_time')
        return context

class CounterpartyDetail(TemplateView):
    template_name = 'counterparties/detail_counterparty.html'
    success_url = reverse_lazy('counterparties_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['counterparty'] = get_object_or_404(Counterparties, pk=self.kwargs['pk'])
        context['news_list'] = News.objects.filter(counterparty=self.kwargs['pk'])
        return context


class TuneUpList(TemplateView):
    template_name = 'counterparties/tune_up_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['spark'] = SparkSettings.objects.all()
        context['notification'] = NotificationSettings.objects.all()
        context['source'] = SourceSettings.objects.all()
        return context

