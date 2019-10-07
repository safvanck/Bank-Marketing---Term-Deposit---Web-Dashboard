from django.shortcuts import render
from django.views.generic import TemplateView
from . import plots


class IndexPage(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPage,
                        self).get_context_data(**kwargs)

        context['time1'] = '12:00am'
        return context


class AnalyticsDashboard(TemplateView):
    template_name = 'plot.html'

    def get_context_data(self, **kwargs):
        context = super(AnalyticsDashboard,
                        self).get_context_data(**kwargs)

        context['piechart1'] = plots.pie_chart_subscibed()
        context['piechart2'] = plots.pie_chart_not_subscribed()
        context['scatterplot'] = plots.scatter_plot_all()
        context['plot2'] = plots.plot2()
        context['plot3'] = plots.plot3()
        context['data_heatmap'] = plots.data_heatmap()

        return context
