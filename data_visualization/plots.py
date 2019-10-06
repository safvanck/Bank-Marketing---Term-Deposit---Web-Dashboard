
import requests
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
from datetime import datetime
from .data_utils.process_data import (
    job_pie_diagram_subscribed, job_pie_diagram_not_subscribed, make_scatter_plot, get_data_heatmap, get_data)


data_df = get_data()


def pie_chart_subscibed():
    labels, values = job_pie_diagram_subscribed(data_df)
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    plot_div = plot(fig, output_type='div', filename='pichrt2')
    return plot_div


def pie_chart_not_subscribed():
    labels, values = job_pie_diagram_not_subscribed(data_df)
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])

    plot_div = plot(fig, output_type='div', filename='piechart')
    return plot_div


def scatter_plot_all():
    return make_scatter_plot(data_df)


def data_heatmap():
    x, y, z = get_data_heatmap(data_df)
    fig = go.Figure(data=go.Heatmap(z=z, y=y, x=x))

    plot_div = plot(fig, output_type='div', filename='heatmap')
    return plot_div
