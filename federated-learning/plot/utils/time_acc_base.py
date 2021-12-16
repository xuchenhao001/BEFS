# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager
from cycler import cycler
import pylab

# input latex symbols in matplotlib
# https://stackoverflow.com/questions/43741928/matplotlib-raw-latex-epsilon-only-yields-varepsilon
plt.rcParams["mathtext.fontset"] = "cm"


# Plot number in a row: "2", "3", "4"
# 2: Two plots in a row (the smallest fonts)
# 3: Three plots in a row
# 4: Four plots in a row (the biggest fonts)
def get_font_settings(size):
    if size == "2":
        font_size_dict = {"l": 21, "m": 18, "s": 16}
        fig_width = 8  # by default is 6.4 x 4.8
        fig_height = 4
    elif size == "3":
        font_size_dict = {"l": 25, "m": 21, "s": 19}
        fig_width = 8
        fig_height = 4
    else:
        font_size_dict = {"l": 25, "m": 25, "s": 20}
        fig_width = 6.4
        fig_height = 4.8

    xy_label_font = font_manager.FontProperties(
        family='Times New Roman', weight='bold', style='normal', size=font_size_dict["l"])
    title_font = font_manager.FontProperties(
        family='Times New Roman', weight='bold', style='normal', size=font_size_dict["m"])
    legend_font = font_manager.FontProperties(
        family='Times New Roman', weight='bold', style='normal', size=font_size_dict["s"])
    ticks_font = font_manager.FontProperties(family='Times New Roman', style='normal', size=font_size_dict["s"])
    cs_xy_label_font = {'fontproperties': xy_label_font}
    cs_title_font = {'fontproperties': title_font}
    cs_xy_ticks_font = {'fontproperties': ticks_font}
    font_factory = {
        'legend_font': legend_font,
        'cs_xy_label_font': cs_xy_label_font,
        'cs_title_font': cs_title_font,
        'cs_xy_ticks_font': cs_xy_ticks_font,
        'fig_width': fig_width,
        'fig_height': fig_height,
    }
    return font_factory


def get_cycle_settings():
    # color names: https://matplotlib.org/stable/gallery/color/named_colors.html
    # colors = plt.get_cmap('tab10').colors  # by default
    colors = ("tab:blue",) + plt.get_cmap('Set2').colors
    # colors = [plt.cm.Spectral(i / float(6)) for i in range(6)]
    # colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive']

    markers = ["D", "o", "^", "s", "*", "X", "d", "x", "1"]
    # my_cycler = cycler(color=colors, marker=markers)
    my_cycler = cycler(color=colors)
    return my_cycler


def plot_time_acc(title, fed_sync_sgd, fed_efsign, fed_sign_sgd, fed_avg, local_train, in_legend=False, ex_legend=False, save_path=None, plot_size="2"):
    font_settings = get_font_settings(plot_size)
    cycle_settings = get_cycle_settings()
    x = range(1, len(fed_sync_sgd) + 1)

    fig, axes = plt.subplots()
    axes.set_prop_cycle(cycle_settings)

    axes.plot(x, fed_sync_sgd, label="BEFS", linewidth=4.5, zorder=10)
    axes.plot(x, fed_efsign, label="EF-signSGD")
    axes.plot(x, fed_sign_sgd, label="SignSGD")
    axes.plot(x, fed_avg, label="FedAvg")
    axes.plot(x, local_train, label="Local")

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Accuracy (%)", **font_settings.get("cs_xy_label_font"))

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.xlim(0, xrange)
    if in_legend:
        plt.legend(prop=font_settings.get("legend_font"), loc='lower right').set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    if ex_legend:
        plot_legend_head(axes, 5, 20.6, 0.7, save_path, plot_size)


def plot_time_acc_ablation(title, bc_ns, bc_FedAvg, ns, in_legend=False, ex_legend=False, save_path=None, plot_size="2"):
    font_settings = get_font_settings(plot_size)
    cycle_settings = get_cycle_settings()
    x = range(1, len(bc_ns) + 1)

    fig, axes = plt.subplots()
    axes.set_prop_cycle(cycle_settings)

    axes.plot(x, bc_ns, label="BC+NS (BEFS)", linewidth=4.5, zorder=10)
    axes.plot(x, bc_FedAvg, label="BC+FedAvg")
    axes.plot(x, ns, label="NS")

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Accuracy (%)", **font_settings.get("cs_xy_label_font"))

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.xlim(0, xrange)
    if in_legend:
        plt.legend(prop=font_settings.get("legend_font"), loc='lower right').set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    if ex_legend:
        plot_legend_head(axes, 3, 20.6, 0.7, save_path, plot_size)


def plot_time_acc_sensitivity(title, lr_1, lr_01, lr_001, save_path=None, plot_size="2"):
    font_settings = get_font_settings(plot_size)
    cycle_settings = get_cycle_settings()
    x = range(1, len(lr_1) + 1)

    fig, axes = plt.subplots()
    axes.set_prop_cycle(cycle_settings)

    axes.plot(x, lr_01, label="lr=0.01", linewidth=4.5, zorder=10)
    axes.plot(x, lr_1, label="lr=0.1")
    axes.plot(x, lr_001, label="lr=0.001")

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Accuracy (%)", **font_settings.get("cs_xy_label_font"))

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.xlim(0, xrange)
    plt.legend(prop=font_settings.get("legend_font"), loc='lower right').set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()


def plot_time_acc_attack(title, fed_sync_sgd, fed_ecsign, fed_efsign, fed_mvsign, fed_rlrsign, fed_avg, fed_err,
                         fed_lfr, in_legend=False, ex_legend=False, save_path=None, plot_size="2"):
    font_settings = get_font_settings(plot_size)
    cycle_settings = get_cycle_settings()
    x = range(1, len(fed_sync_sgd) + 1)

    fig, axes = plt.subplots()
    axes.set_prop_cycle(cycle_settings)

    axes.plot(x, fed_sync_sgd, label="BEFS", linewidth=4.5, zorder=10)
    axes.plot(x, fed_ecsign, label="EC-signSGD")
    axes.plot(x, fed_efsign, label="EF-signSGD")
    axes.plot(x, fed_mvsign, label="MV-signSGD")
    axes.plot(x, fed_rlrsign, label="RLR-signSGD")
    axes.plot(x, fed_err, label="ERR-FedAvg")
    axes.plot(x, fed_lfr, label="LFR-FedAvg")
    axes.plot(x, fed_avg, label="FedAvg")

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Accuracy (%)", **font_settings.get("cs_xy_label_font"))

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.xlim(0, xrange)
    if in_legend:
        plt.legend(prop=font_settings.get("legend_font"), loc='lower right').set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    if ex_legend:
        plot_legend_head(axes, 8, 20.6, 0.7, save_path, plot_size)


def plot_time_acc_fall(title, fed_sync_sgd, fed_efsign, fed_avg, save_path=None, plot_size="2"):
    font_settings = get_font_settings(plot_size)
    cycle_settings = get_cycle_settings()
    x = range(1, len(fed_sync_sgd) + 1)

    fig, axes = plt.subplots()
    axes.set_prop_cycle(cycle_settings)

    axes.plot(x, fed_sync_sgd, label="BEFS", linewidth=4.5, zorder=10)
    axes.plot(x, fed_efsign, label="ARE")
    axes.plot(x, fed_avg, label="FedAvg")

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Accuracy (%)", **font_settings.get("cs_xy_label_font"))

    plt.title(title, **font_settings.get("cs_title_font"))
    plt.xticks(**font_settings.get("cs_xy_ticks_font"))
    plt.yticks(**font_settings.get("cs_xy_ticks_font"))
    plt.tight_layout()
    # plt.xlim(0, xrange)
    plt.legend(prop=font_settings.get("legend_font")).set_zorder(11)
    plt.grid()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()


def plot_time_bar(title, sgd, sign_sgd, save_path=None, plot_size="2"):
    font_settings = get_font_settings(plot_size)
    x = ["CNN-CIFAR10", "CNN-FMNIST", "MLP-FMNIST"]

    # fig, axes = plt.subplots()
    fig, axes = plt.subplots(1, 3, tight_layout=True)

    width = 0.15  # the width of the bars
    axes[0].bar(0 - width / 2, height=sgd[0], width=width, label="SGD",
                hatch='x')
    axes[0].bar(0 + width / 2, height=sign_sgd[0], width=width, label="SignSGD", hatch='*')

    axes[1].bar(0 - width / 2, height=sgd[1], width=width, label="SGD",
                hatch='x')
    axes[1].bar(0 + width / 2, height=sign_sgd[1], width=width, label="SignSGD", hatch='*')

    axes[2].bar(0 - width / 2, height=sgd[2], width=width, label="SGD",
                hatch='x')
    axes[2].bar(0 + width / 2, height=sign_sgd[2], width=width, label="SignSGD", hatch='*')

    for i in range(len(axes)):
        # Use the pyplot interface to change just one subplot
        plt.sca(axes[i])
        plt.grid()
        plt.xticks([0], [x[i]], **font_settings.get("cs_xy_ticks_font"))
        plt.yticks(**font_settings.get("cs_xy_ticks_font"))

    fig.supxlabel("The Type of Model and Datasets", **font_settings.get("cs_xy_label_font"))
    fig.supylabel("Gradient Size (MB)", **font_settings.get("cs_xy_label_font"))
    fig.suptitle(title, **font_settings.get("cs_title_font"))

    plt.subplots_adjust(top=1.9)
    handles, labels = axes[2].get_legend_handles_labels()
    fig.legend(handles, labels, loc='upper center', prop=font_settings.get("legend_font"), ncol=2)
    # fig.legend(handles, labels, prop=font_settings.get("legend_font"), ncol=2, bbox_to_anchor=(1.0, 1.05))
    # fig.legend(handles, labels, loc='upper right', prop=font_settings.get("legend_font"))

    fig.tight_layout()
    fig.set_size_inches(font_settings.get("fig_width"), font_settings.get("fig_height"))
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()


def plot_legend_head(axes, legend_column, width, height, save_path=None, plot_size="3"):
    font_settings = get_font_settings(plot_size)
    figlegend = pylab.figure()
    figlegend.legend(axes.get_legend_handles_labels()[0], axes.get_legend_handles_labels()[1],
                     prop=font_settings.get("legend_font"), ncol=legend_column, loc='upper center')
    figlegend.tight_layout()
    figlegend.set_size_inches(width, height)
    if save_path:
        save_path = save_path[:-4] + "-legend.png"
        figlegend.savefig(save_path)
    else:
        figlegend.show()
