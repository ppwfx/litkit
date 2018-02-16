import pandas as pd
import numpy as np

import plotly.offline as py
import plotly.figure_factory as ff


def scatter_matrix(df):
    fig = ff.create_scatterplotmatrix(df, diag='box', height=1000, width=1900)
    py.plot(fig, filename='/tmp/scatter_matrix.html')
