import matplotlib.pyplot as plt
from matplotlib.legend import Legend

def extract_lines():
    parent_figure = plt.gcf()
    parent_ax = plt.gca()
    xlim = parent_ax.get_xlim()
    ylim = parent_ax.get_ylim()
    lines = parent_ax.get_lines()
    for i, line in enumerate(lines):
        line.remove()

        plt.figure()
        plt.gca().set_xlim(xlim)
        plt.gca().set_ylim(ylim)
        plt.gca().add_artist(line)
        plt.gca().axis('off')
        plt.savefig("line_{}.png".format(i), transparent=True)
        plt.close()
        line.remove()
        parent_figure.add_artist(line)

def extract_frame():
    parent_figure = plt.gcf()
    ax = plt.gca()

    ax.remove()
    fig = plt.figure()
    ax.figure = fig
    fig.axes.append(ax)
    fig.add_axes(ax)
    plt.savefig("axes.png", transparent=True)
    plt.close()
    ax.remove()
    ax.figure = parent_figure
    parent_figure.axes.append(ax)
    parent_figure.add_axes(ax)

def extract_legend():
    parent_figure = plt.gcf()
    legends = [c for c in plt.gca().get_children() if isinstance(c, Legend)]
    for i, legend in enumerate(legends):
        legend.remove()
        
        plt.figure()
        plt.gca().add_artist(legend)
        plt.gca().axis('off')
        plt.savefig("legend_{}.png".format(i), transparent=True)
        plt.close()
        legend.remove()
        parent_figure.add_artist(legend)

def extract_elements():
    extract_lines()
    extract_legend()
    extract_frame()
