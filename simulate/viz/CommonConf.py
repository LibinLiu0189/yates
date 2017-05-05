import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as pp
import numpy as np
import scipy.stats as sp

def gen_label (scm):
    names = {"ac" : "AC",
            "ecmp" : "ECMP",
            "edksp" : "EDKSP",
            "ffc" : "FFCksp",
            "ffced" : "FFC",
            "ksp" : "KSP",
            "mcf" : "MCF",
            "optimalmcf" : "Optimal",
            "raeke" : r"""$R\"acke$""",
            "raecke" : r"""$R\"acke$""",
            "semimcfedksp" : "SMOEDK",
            "semimcfksp" : "SWAN",
            "semimcfmcfftenv" : "Joint",
            "semimcfraeke" : "SMORE",
            "spf" : "SPF",
            "vlb" : "VLB",
            }
    return names.get(scm, scm)

solver_list = ['ecmp', 'raeke', 'semimcfmcfftenv', 'semimcfksp', 'ffced', 'semimcfraeke', 'optimalmcf']

markevery = 2

#start_tm = 4
#end_tm = 11
width=4
height=3
#xlabels = range(1, end_tm-start_tm+2)
left_plot='base'

def setupMPPDefaults():
    pp.rcParams['font.size'] = 28
    pp.rcParams['mathtext.default'] = 'regular'
    pp.rcParams['ytick.labelsize'] = 24
    pp.rcParams['xtick.labelsize'] = 24
    pp.rcParams['legend.fontsize'] = 20
    pp.rcParams['lines.markersize'] = 12
    pp.rcParams['axes.titlesize'] = 24
    pp.rcParams['axes.labelsize'] = 24
    pp.rcParams['axes.edgecolor'] = 'grey'
    pp.rcParams['axes.linewidth'] = 3.0
    pp.rcParams['axes.grid'] = True
    pp.rcParams['grid.alpha'] = 0.4
    pp.rcParams['grid.color'] = 'grey'
    pp.rcParams['legend.frameon'] = True
    pp.rcParams['legend.framealpha'] = 0.4
    pp.rcParams['legend.numpoints'] = 1
    pp.rcParams['legend.scatterpoints'] = 1

def getLineMarkersDict():
   return {
           'ecmp'   : '+',
           'spf'   : 'x',
           'semimcfksp'    : '<',
           'semimcfedksp'    : 's',
           'ac'    : 'o',
           'edksp'    : 'x',
           'semimcfraeke'    : 'v',
           'semimcfmcfftenv'  : '>',
           'raeke' : 'o',
           'optimalmcf'     : '.',
           'mcf'    : 'd',
           'vlb'    : 's',
           'ksp'    : 'd',
           'ffc'    : '.',
           'ffced'    : 'x',
           }

def getHatchDict():
   return {
           'ecmp'   : '+',
           'spf'   : '+',
           'semimcfksp'    : '/',
           'semimcfedksp'    : 's',
           'ac'    : '-',
           'edksp'    : 'x',
           'semimcfraeke'    : '-',
           'semimcfmcfftenv'  : '\\',
           'raeke' : 'o',
           'optimalmcf'     : '.',
           'mcf'    : '*',
           'vlb'    : 's',
           'ksp'    : '*',
           'ffc'    : '*',
           'ffced'    : 'o',
           }

def getLineMarkersLWDict():
   return {
           'ecmp'   : 5,
           'spf'   : 5,
           'semimcfksp'    : 5,
           'semimcfedksp'    : 5,
           'ac'    : 5,
           'edksp'    : 5,
           'semimcfraeke'    : 5,
           'semimcfmcfftenv'  : 5,
           'raeke' : 5,
           'optimalmcf'     : 5,
           'mcf'    : 5,
           'vlb'    : 5,
           'ksp'    : 5,
           'ffc'    : 5,
           'ffced'    : 5,
           }

def getLineMarkersSizeDict():
   return {
           'ecmp'           : 14,
           'spf'           : 14,
           'semimcfksp'     : 14,
           'semimcfedksp'     : 10,
           'ac'     : 10,
           'edksp'     : 14,
           'semimcfraeke'     : 14,
           'semimcfmcfftenv'  : 14,
           'raeke'          : 14,
           'optimalmcf'     : 14,
           'mcf'            : 14,
           'vlb'            : 14,
           'ksp'            : 14,
           'ffc'            : 14,
           'ffced'            : 10,
           }

def getLineColorsDict():
    return {
           'ecmp'   : 'purple',
           'spf'   : 'blue',
           'semimcfksp'    : 'navy',
           'semimcfedksp'    : 'green',
           'ac'    : 'green',
           'edksp'    : 'dodgerblue',
           'semimcfraeke'    : 'red',
           'semimcfmcfftenv'  : 'dimgrey',
           'raeke' : 'coral',
           'optimalmcf'     : 'black',
           'mcf'    : 'darkgreen',
           'vlb'    : 'dimgrey',
           'ksp'    : 'blue',
           'ffc'    : 'gray',
           'ffced'    : 'dodgerblue',
           }

def getLineFormatsDict():
    return {
           'ecmp'   : '--',
           'spf'   : '--',
           'semimcfksp'    : '-',
           'semimcfedksp'    : '-',
           'ac'    : '--',
           'edksp'    : '-',
           'semimcfraeke'    : '-',
           'semimcfmcfftenv'  : '--',
           'raeke' : '--',
           'optimalmcf'     : ':',
           'mcf'    : '-',
           'vlb'    : '--',
           'ksp'    : '--',
           'ffc'    : '-',
           'ffced'    : '-',
           }


def create_legend():
    colors=getLineColorsDict()
    mrkrs=getLineMarkersDict()
    mrkrsize = getLineMarkersSizeDict()
    fig = pp.figure()
    figlegend = pp.figure(figsize=(18,0.6))
    ax = fig.add_subplot(111)
    handles = []
    props = dict(alpha=0.6, edgecolors='none' )
    for solver in solver_list:
        handles.append(ax.scatter([1], [1], c=colors[solver],
            marker=mrkrs[solver],
            linewidths=mrkrsize[solver]/3,
            s=400, **props))

    figlegend.legend(handles, [gen_label(x) for x in solver_list],loc=4, ncol=8)
    figlegend.savefig('legend.pdf')

def plot_scatter(congs, tputs, y_lim, x_lim, plot_file,x_label,y_label,allow_legend,set_label=False):
    setupMPPDefaults()
    #if allow_legend and left_plot in plot_file:
    #    fig = pp.figure(figsize=(width+0.5,height))
    #else:
    #    fig = pp.figure(figsize=(width,height))
    fig = pp.figure(figsize=(width+0.5,height))
    ax = fig.add_subplot(111)
    props = dict(alpha=0.6, edgecolors='none' )
    colors=getLineColorsDict()
    mrkrs=getLineMarkersDict()
    mrkrsize = getLineMarkersSizeDict()
    handles = []
    slist = solver_list
    if 'ffc' in slist:
      slist.remove('ffc')
    #if 'semimcfedksp' in slist:
    #  slist.remove('semimcfedksp')
    for solver in slist:
        if len(congs.get(solver,[])) == 0:
            continue
        x = np.mean(np.asarray(congs[solver]))
        y = np.mean(np.asarray(tputs[solver]))
        #ax.errorbar([x],[y],xerr=[(0-0*min(congs[solver]), max(congs[solver])-x)], yerr=[(y-min(tputs[solver]), max(tputs[solver])-x)])
        if False:
            pts = geo.MultiPoint(zip(x,y))
            hull = pts.convex_hull
            print hull
            patch = PolygonPatch(hull,fc=colors[solver], ec=colors[solver], fill=True, zorder=-1, alpha=0.2)
            ax.add_patch(patch)
        handles.append(ax.scatter(x, y, c=colors[solver],
            marker=mrkrs[solver],
            linewidths=mrkrsize[solver]/3,
            s=400, **props))
    # mark regions in graph
    #if "scale3" in plot_file:
    if False:
        ax.annotate('high tput\nlow cong', color='green', xy=(.2, .9), xycoords='axes fraction', horizontalalignment='center', verticalalignment='center')
        ax.annotate('low tput\nlow cong', color='orangered', xy=(.2, .2), xycoords='axes fraction', horizontalalignment='center', verticalalignment='center')
        ax.annotate('high tput\nhigh cong', color='y', xy=(.68, .9), xycoords='axes fraction', horizontalalignment='center', verticalalignment='center')
        ax.annotate('low tput\nhigh cong', color='red', xy=(.8, .2), xycoords='axes fraction', horizontalalignment='center', verticalalignment='center')
    #ax.plot((0, 1), color='gray',linestyle="--",alpha=0.5)
    if set_label:
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
    if left_plot in plot_file:
        #ax.set_ylabel(y_label)
        if allow_legend:
            #ax.legend(handles, [gen_label(x) for x in solver_list],loc=4, ncol=2)
            pass
    #ax.set_aspect(1./ax.get_data_ratio())
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.locator_params(axis='x', nbins=5)
    ax.locator_params(axis='y', nbins=5)
    pp.xlim(x_lim)
    pp.ylim(y_lim)
    pp.tight_layout()
    pp.savefig("scatter-"+plot_file)

def plot_bar (scm_data, plot_file, y_lim, y_label, allow_legend):
    setupMPPDefaults()
    colors = getLineColorsDict()
    patterns = getHatchDict()
    fig = pp.figure(figsize=(width,height))
    ax = fig.add_subplot(111)
    bar_width = 0.7
    n_groups = len(solver_list)
    metric_val = [np.mean(np.asarray(scm_data[scm])) for scm in solver_list]
    index = np.arange(n_groups)
    rects = ax.bar(index, metric_val, bar_width, color='white', edgecolor=[colors[x] for x in solver_list], align='center')
    for (solver,bar) in zip(solver_list, rects):
        bar.set_hatch(patterns[solver])

    if left_plot in plot_file:
      ax.set_ylabel(y_label);
      if allow_legend:
        ax.legend(rects, [gen_label(x) for x in solver_list])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    pp.xticks(range(len(solver_list)), [' ' for x in solver_list])
    ax.locator_params(axis='y', nbins=6)
    pp.ylim(y_lim)
    pp.tight_layout()
    pp.savefig("bar-"+plot_file)

def plot_box (scm_data, plot_file, y_lim, y_label):
    setupMPPDefaults()
    colors = getLineColorsDict()
    mrkrs = getLineMarkersDict()
    fig = pp.figure(figsize=(width,height))
    ax = fig.add_subplot(111)
    bar_width = 0.5
    n_groups = len(scm_data)
    metric_val = [np.asarray(scm_data[scm]) for scm in solver_list]
    bp = ax.boxplot(metric_val,
            notch=False,
            showmeans=True, meanline=True,
            patch_artist=True)
    for (solver,box) in zip(solver_list, bp['boxes']):
        box.set(color=colors[solver])
        box.set_facecolor(colors[solver])

    if left_plot in plot_file:
      ax.set_ylabel(y_label);
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    pp.xticks(range(len(solver_list)), [' ' for x in solver_list])
    ax.locator_params(axis='y', nbins=6)
    pp.ylim(y_lim)
    pp.tight_layout()
    pp.savefig("box-"+plot_file)

def plot_line (dirn, fname, xs, ysPerSolver, ydevsPerSolver, y_lim, x_label, y_label, allow_legend):
  setupMPPDefaults()
  fmts = getLineFormatsDict()
  mrkrs = getLineMarkersDict()
  mrkrsize = getLineMarkersSizeDict()
  mrkrlw = getLineMarkersLWDict()
  colors = getLineColorsDict()
  #xticks = range(start_tm, end_tm+1)
  #xlabels = range(1,end_tm-start_tm+2)
  fig = pp.figure(figsize=(width,height))
  ax = fig.add_subplot(111)
  for solver in solver_list:
    ys = ysPerSolver[solver]
    xs_arr = np.asarray(xs)
    avg_y,std_y = np.mean(np.asarray(ys)), np.std(np.asarray(ys))
    ax.plot(xs_arr, ys,
            label=gen_label(solver),
            marker=mrkrs[solver],
            markersize=mrkrsize[solver],
            markerfacecolor='none',
            markeredgecolor=colors[solver],
            markeredgewidth=mrkrsize[solver]/4,
            linestyle=fmts[solver],
            alpha=1,
            color = colors[solver],
            markevery = markevery,
            linewidth = mrkrlw[solver])

  ax.set_xlabel(x_label);
  if left_plot in dirn:
    ax.set_ylabel(y_label);
    if allow_legend:
      ax.legend(loc=3, borderaxespad=0., fancybox=True, ncol=1)
  #pp.xlim(start_tm,end_tm)
  pp.ylim(y_lim)
  ax.spines['right'].set_visible(False)
  ax.spines['top'].set_visible(False)
  ax.yaxis.set_ticks_position('left')
  ax.xaxis.set_ticks_position('bottom')
  #ax.set_xticklabels(xlabels)
  ax.locator_params(axis='y', nbins=4)
  #pp.xticks(xticks, xlabels)
  pp.tight_layout()
  pp.savefig("line-"+dirn+"_"+fname+".pdf")


