
import requests
import pandas as pd
import plotly.graph_objs as go
from plotly.offline import plot
from datetime import datetime
from .data_utils.process_data import (
    job_pie_diagram_subscribed, job_pie_diagram_not_subscribed, make_scatter_plot, get_data_heatmap, get_plot2, get_plot3, get_data)


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


def plot2():
    x, y = get_plot2(data_df)
    layout = go.Layout()
    layout.xaxis.title = 'Age (Years)'
    layout.yaxis.title = 'Avg Yearly Balance (in Euros)'
    fig = go.Figure(layout_title_text="Age vs Avg Yearly Balance",layout=layout)
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="markers",
        marker=go.scatter.Marker(
            size=4,
            color=45,
            opacity=0.6,
            colorscale="Viridis"
        )))

    plot_div = plot(fig, output_type='div', filename='age-y')
    return plot_div


def plot3():
    labels, values = get_plot3(data_df)
    layout = go.Layout()
    layout.xaxis.title = 'Age (Years)'
    layout.yaxis.title = 'Last campaign call duration (in Seconds)'

    fig = go.Figure(
        data=[go.Bar(x=labels, y=values)],
        layout_title_text="Age vs Last campaign call duration",
        layout=layout
    )

    plot_div = plot(fig, output_type='div', filename='age-duration')
    return plot_div


def plot4():

    x0 = data_df[data_df['y'] == 'yes']['age']
    x1 = data_df[data_df['y'] == 'no']['age']
    trace0 = go.Histogram(
        x=x0, name='Subscribed'
    )
    trace1 = go.Histogram(
        x=x1, name='Not Subscrbed'
    )
    data = [trace0, trace1]
    layout = go.Layout(barmode='stack')
    layout.xaxis.title = 'Age (Years)'
    layout.yaxis.title = '# of People'
    fig = go.Figure(data=data, layout=layout,
                    layout_title_text='Age Histogram by Subscription',)
    plot_div = plot(fig, output_type='div',
                    filename='stacked histogram-age-vs_subscription')
    return plot_div
