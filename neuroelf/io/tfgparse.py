__version__ = '0.0.1'
__build__ = 20111814

import sys
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

import pandas as pd

def _parseval(v):
    try:
        v = v[1:].strip().split(' ')
        if not v:
            return []
        if v[0] == '[' and v[-1] == ']':
            v = v[1:-1]
        v = [float(val) for val in v if val.strip()]
        v = [int(val) if float(int(val)) == val else val for val in v]
    except Exception as e:
        print(str(e))
    return v

def tfgparse(filename):

    # setup elements
    figure = {s: None for s in [
        'COMMENTS', 'VARIABLES', 'FIGURE', 'MENU', 'UIMENU', 'UICONTROLS',
    ]}
    nl = '\n'
    try:
        with open(filename, 'r') as tfid:
            fcont = tfid.read().strip()
            flines = [l.strip() for l in fcont.split(nl) if l.strip()]
    except Exception as e:
        print(str(e))
        return figure
    
    # find sections
    sections = {}
    in_section = ''
    for li, l in enumerate(flines):
        if not in_section:
            if not ('---' in l and 'BEGIN_' in l):
                continue
            for s in figure.keys():
                if s.upper() in l:
                    in_section = s.upper()
                    begin_line = li + 1
                    break
            continue
        if '---' in l and f'END_{in_section}' in l:
            sections[in_section] = [begin_line, li]
            in_section = ''
    if in_section:
        sections[in_section] = [begin_line, li+1]
    
    # store in figure
    for s, sl in sections.items():
        slines = flines[sl[0]:sl[1]]
        try:
            figure[s] = pd.read_csv(StringIO('\n'.join(slines)), sep='|')
        except:
            print(f'Error processing section {s}: {nl.join(slines)}')
    
    # post-processing
    for s in figure.keys():
        sc = figure[s]
        if sc is None:
            continue

        # strip column names
        sc = sc.rename(columns={c: c.strip() for c in sc.columns})

        # evaluate numeric arrays
        for c in sc.columns:
            for ri in range(sc.shape[0]):
                v = sc.loc[ri,c]
                if not isinstance(v, str):
                    continue
                v = v.strip()
                if v and v[0] == '$':
                    v = _parseval(v)
                try:
                    if s != 'FIGURE':
                        sc.loc[ri,c] = v
                    else:
                        sc[c] = [v]
                except Exception as e:
                    print(str(e))

        # only return pertinent rows
        if s == 'UICONTROLS':
            sc = sc[sc.Type != '']
        
        # set back
        figure[s] = sc
    
    # return content
    return figure
