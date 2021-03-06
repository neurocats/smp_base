"""Some plotting utils"""

import matplotlib.pyplot as plt
from matplotlib import rc
from matplotlib import rcParams
from matplotlib.font_manager import FontProperties

def set_latex_header():
    # plotting parameters
    rc('text', usetex=True)
    rc('font', serif="Times New Roman")
    rc('font', family='serif')
    rc('font', style="normal",
    variant="normal", weight=700,
    stretch="normal", size=10.0)
    rcParams["text.latex.preamble"] = r"\usepackage{amsmath}\usepackage{amsfonts}\usepackage{amssymb}\usepackage{latexsym}\usepackage{bm}"

def set_fontprops():
    fontP = FontProperties()
    fontP.set_size('small')
    return fontP

def ax_check(ax = None):
    if ax is None:
        ax = plt.gca()
    return ax

def resize_panel_vert(resize_by = 0.8, ax = None):
    ax = ax_check(ax)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width * resize_by, box.height])
    
def resize_panel_horiz(resize_by = 0.8, ax = None):
    ax = ax_check(ax)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0, box.width, box.height * resize_by])

def custom_legend(labels = None, resize_by = 0.8, ax = None, loc = 'right', lg = None):
    if loc == 'right' or loc == 'left':
        put_legend_out_right(labels = labels, resize_by = resize_by, ax = ax, right = loc, lg = lg)
    elif loc in ['upper', 'top'] or loc == 'lower':
        put_legend_out_top(labels = labels, resize_by = resize_by, ax = ax, top = loc, lg = lg)
    elif type(loc) is tuple:
        put_legend_out(labels = labels, resize_by = resize_by, ax = ax, loc = loc, lg = lg)

def put_legend_out(labels = None, resize_by = 0.8, ax = None, loc = None, lg = None):
    ax = ax_check(ax)
    if loc[0] < 0.1 or loc[0] > 0.9:
        resize_panel_vert(resize_by = resize_by, ax = ax)
    if loc[1] < 0.1 or loc[1] > 0.9:
        resize_panel_horiz(resize_by = resize_by, ax = ax)
        
    if labels is None:
        ax.legend(loc = loc, ncol=1)
    else:
        ax.legend(loc = loc, ncol=1, labels = labels)

def put_legend_out_right(labels = None, resize_by = 0.8, ax = None, right = 'left', lg = None):
    ax = ax_check(ax)
    resize_panel_vert(resize_by = resize_by, ax = ax)
    loc = 'upper %s' % (right, )
    if lg is None:
        bboxy = 0.95
    else:
        bboxy = 0.5
        
    if right == 'left':
        bbox = (1.1, bboxy)
    elif right == 'right':
        bbox = (-0.25, bboxy)
    # loc = 'center left'
    # bbox = (1.0, 0.5)
    if labels is None:
        ax.legend(loc = loc, bbox_to_anchor = bbox, ncol=1)
    else:
        ax.legend(loc = loc, bbox_to_anchor = bbox, ncol=1, labels = labels)

def put_legend_out_top(labels = None, resize_by = 0.8, ax = None, top = 'lower', lg = None):
    ax = ax_check(ax)
    resize_panel_horiz(resize_by = resize_by, ax = ax)
    loc = '%s center' % (top, )
    if lg is None:
        bboxx = 0.1
    else:
        bboxx = 0.5

    if top == 'upper':
        bbox = (bboxx, -0.1) #
    elif top == 'lower':
        bbox = (bboxx, 1.1) #
    if labels is None:
        ax.legend(loc = loc, bbox_to_anchor = bbox, ncol=10)        
    else:
        ax.legend(loc = loc, bbox_to_anchor = bbox, ncol=10, labels = labels)

