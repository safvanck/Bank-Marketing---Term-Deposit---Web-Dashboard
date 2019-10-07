import pandas as pd
import numpy as np
from .variables import dataset_path


def get_data():
    data_df = pd.read_csv(dataset_path, sep=';')
    return data_df


def job_pie_diagram_subscribed(data_df):
    df = data_df.loc[data_df['y'] == 'yes']
    tJobCount = df.groupby('job')['job'].count()
    return list(map(str.upper, tJobCount.keys())), tJobCount.values


def job_pie_diagram_not_subscribed(data_df):
    df = data_df.loc[data_df['y'] == 'no']
    tJobCount = df.groupby('job')['job'].count()
    return list(map(str.upper, tJobCount.keys())), tJobCount.values


def make_scatter_plot(data_df):
    pSctter = pd.plotting.scatter_matrix(data_df)
    return pSctter


def get_data_heatmap(data_df):
    corr = data_df.corr()
    z = corr.values
    y = list(map(str.upper, corr.columns))
    x = list(map(str.upper, corr.columns))
    return x, y, z


def get_plot2(data_df):
    age = list(data_df['age'])
    balance = list(data_df['balance'])
    return age, balance


def get_plot3(data_df):
    age = list(data_df['age'])
    duration = np.array(data_df['duration']) / 60
    return age, duration
