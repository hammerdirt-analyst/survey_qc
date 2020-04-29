import matplotlib.dates as mdates
from matplotlib import cm
from matplotlib import colors as mcolors
import matplotlib.pyplot as plt
from utilities.utility_functions import save_the_figure as save_the_figure
import numpy as np
from matplotlib.patches import Circle

def scatterPlot(**kwargs):

    fig, ax = plt.subplots(figsize=(8,5))
    if kwargs['date_range'] == 'All':
        a_df = kwargs['a_df']
        number_of_samples= len(kwargs['a_df'])
        locations = a_df.location.unique()
        number_of_locations = len(locations)
    else:
        a_df = kwargs['a_df']
        date_range = kwargs['date_range']
        a_df = a_df.loc[(a_df.py_date >= date_range[0]) & (a_df.py_date <= date_range[1])]
        number_of_samples= len(kwargs['a_df'])
        locations = a_df.location.unique()
        number_of_locations = len(locations)

    # provide a color map https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
    colors_one = plt.cm.tab20b(np.linspace(0, 1 ,20))
    colors_two = plt.cm.tab20c(np.linspace(0, 1 ,20))
    colors = np.vstack((colors_one, colors_two))



    my_z_scales = []
    my_x_scales = []
    for i,location in enumerate(locations):
        this_df = a_df.loc[a_df.location == location]
        x = this_df[kwargs['x']]
        y = this_df[kwargs['y']]
        z = this_df[kwargs['z']]
        for value in z.values:
            my_z_scales.append(value)
        for value in x.values:
            my_x_scales.append(value)

        ax.scatter(x, y, color=colors[i], s=kwargs['point_size']*z, edgecolor=kwargs['edge_c'], label=location)
    ax.set_axisbelow(True)
    ax.grid(b=True, which='major', axis='both', zorder=0)
    ax.set_xlim(0, max(my_x_scales)+50)

    plt.ylabel(kwargs['y_axis']['label'],
               fontfamily=kwargs['y_axis']['fontfamily'],
               labelpad=kwargs['y_axis']['lablepad'],
               color=kwargs['y_axis']['color'],
               size=kwargs['y_axis']['size']
              )

    plt.xlabel(kwargs['x_axis']['label'],
               fontfamily=kwargs['x_axis']['fontfamily'],
               labelpad=kwargs['x_axis']['lablepad'],
               color=kwargs['x_axis']['color'],
               size=kwargs['x_axis']['size'],
               ha='left',
               linespacing=2,
               x=0,
              )

    plt.subplots_adjust(**kwargs['subplot_params'])
    plt.title(
        kwargs['the_title']['label'],
        fontdict=kwargs['title_style'],
        pad=kwargs['the_title_position']['pad'],
        loc=kwargs['the_title_position']['loc'],
        )
    plt.suptitle(kwargs['the_sup_title']['label'],
                 fontdict=kwargs['sup_title_style'],
                 fontsize=kwargs['sup_title_style']['fontsize'],
                 fontweight=kwargs['sup_title_style']['fontweight'],
                 # color=kwargs['sup_title_style']['color'],
                 x=kwargs['sup_title_position']['x'],
                 y=kwargs['sup_title_position']['y'],
                 va=kwargs['sup_title_position']['va'],
                 ha=kwargs['sup_title_position']['ha']
                )

    lgnd = ax.legend(title='Locations', loc='upper left', bbox_to_anchor=(1.04, 1))
    for handle in lgnd.legendHandles:
        handle.set_sizes([100])


    my_z_s = [min(my_z_scales), max(my_z_scales) ]
    for z in my_z_s:
        plt.scatter([], [], s=kwargs['point_size']*z, c="blue", alpha=0.6, label=' {}pcs/m'.format(z))
    h, l = plt.gca().get_legend_handles_labels()
    plt.legend(h[-2:], l[-2:], labelspacing=2.5, title="Pieces per meter", frameon=True, borderpad=2, loc='lower right')

    plt.gca().add_artist(lgnd)
    # a_min_z = Circle((10,10), z_min*kwargs['point_size'])



    save_the_figure(**kwargs['save_this'])

    plt.show()
    plt.close()
