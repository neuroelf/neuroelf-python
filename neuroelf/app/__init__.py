import os

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_canvas as dc
from dash_canvas.utils import io_utils as dcio

from neuroelf import io as nio
from neuroelf import tools as nt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

basepath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
figfile = basepath + os.sep + '_core' + os.sep + 'figures' + os.sep + 'neuroelf.tfg'
figure = nio.tfgparse(figfile)
components = nt.uicontrols(figure)

app.layout = html.Div(children=components)

__all__ = [
  'app',
  'figure',
]
