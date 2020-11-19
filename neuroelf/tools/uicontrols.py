import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_canvas as dc
from dash_canvas.utils import io_utils as dcio

def uicontrols(figure):
    children = []
    try:
        figpos = figure['FIGURE'].Position[0][:]
        if figpos[0] < 0:
            figpos[0] = 0
        if figpos[1] < 0:
            figpos[1] = 0
        uic = figure['UICONTROLS']
        lastpos = [0, 0, 0, 0]
        for ri, row in uic.iterrows():
            ctype = row.Type
            if not isinstance(ctype, str) or not ctype:
                continue
            ctype = ctype.lower()
            cpos = row.Position[:]
            cposneg = [True if p <= 0 else False for p in cpos]
            if any(cposneg):
                for ci, cp in enumerate(cpos):
                    if ci < 2:
                        cpos[ci] = lastpos[ci] + cpos[ci]
                    elif cpos[ci] == 0:
                        cpos[ci] = lastpos[ci]
                    elif cpos[ci] < 0:
                        cpos[ci] = -cpos[ci]
            lastpos = cpos
            if ctype == 'label':
                children.append(html.Div(
                    children=[html.P(row.Caption)],
                    style={
                        'position': 'fixed',
                        'bottom': cpos[1],
                        'left': cpos[0],
                        'width': f'{cpos[2]}px',
                        'height': f'{cpos[3]}px',
                    }
                ))
    except Exception as e:
        print(str(e))
        return children
    return children
