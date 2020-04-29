import matplotlib.dates as mdates
from matplotlib import cm
from matplotlib import colors as mcolors
import matplotlib.pyplot as plt
from utilities.utility_functions import save_the_figure as save_the_figure
import numpy as np

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




    for i,location in enumerate(locations):
        this_df = a_df.loc[a_df.location == location]
        x = this_df[kwargs['x']]
        y = this_df[kwargs['y']]
        z = this_df[kwargs['z']]
        ax.scatter(x, y, color=colors[i], s=kwargs['point_size'], edgecolor=kwargs['edge_c'])
    ax.set_axisbelow(True)
    ax.grid(b=True, which='major', axis='both', zorder=0)

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
               x=0
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
                 # color=kwargs['sup_title_style']['color'],
                 x=kwargs['sup_title_position']['x'],
                 y=kwargs['sup_title_position']['y'],
                 va=kwargs['sup_title_position']['va'],
                 ha=kwargs['sup_title_position']['ha']
                )



    # years = mdates.YearLocator()
    # months = mdates.MonthLocator()
    # days = mdates.DayLocator()
    # weeks = mdates.WeekdayLocator(byweekday=1, interval=1, tz=None)
    # years_fmt = mdates.DateFormatter(kwargs['x_tick_date']['years'])
    # months_fmt = mdates.DateFormatter(kwargs['x_tick_date']['months'])
    # days_fmt = mdates.DateFormatter(kwargs['x_tick_date']['days'])
    #
    #
    # if(kwargs['ticks'] == 'years'):
    #     ax.xaxis.set_major_locator(years)
    #     ax.xaxis.set_major_formatter(years_fmt)
    #     ax.xaxis.set_minor_locator(months)
    # elif(kwargs['ticks'] == 'months'):
    #     ax.xaxis.set_major_locator(years)
    #     ax.xaxis.set_major_formatter(years_fmt)
    #     ax.xaxis.set_minor_locator(months)
    #     ax.xaxis.set_minor_formatter(months_fmt)
    # elif(kwargs['ticks']== 'days'):
    #     ax.xaxis.set_major_locator(weeks)
    #     ax.xaxis.set_major_formatter(days_fmt)
    #     ax.xaxis.set_minor_locator(days)


    save_the_figure(**kwargs['save_this'])

    plt.show()
    plt.close()
