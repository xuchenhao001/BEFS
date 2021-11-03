# -*- coding: UTF-8 -*-

# For ubuntu env error: findfont: Font family ['Times New Roman'] not found. Falling back to DejaVu Sans.
# ```bash
# sudo apt install msttcorefonts
# rm -rf ~/.cache/matplotlib
# ```
import matplotlib.pyplot as plt
import matplotlib.font_manager as font_manager

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
        fig_width = 7.5  # by default is 6.4 x 4.8
        fig_height = 5
    elif size == "3":
        font_size_dict = {"l": 25, "m": 21, "s": 19}
        fig_width = 7.5
        fig_height = 5
    else:
        font_size_dict = {"l": 25, "m": 25, "s": 25}
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


def plot_time_acc(title, fed_sync_sgd, fed_sync, fed_efsign, fed_avg, local_train, save_path=None, plot_size="2"):
    font_settings = get_font_settings(plot_size)
    x = range(1, len(fed_sync_sgd) + 1)

    fig, axes = plt.subplots()

    axes.plot(x, fed_sync_sgd, label="BEFS-signSGD", linewidth=3, zorder=10)
    axes.plot(x, fed_sync, label="BEFS-SGD")
    axes.plot(x, fed_efsign, label="EF-signSGD")
    axes.plot(x, fed_avg, label="FedAVG")
    axes.plot(x, local_train, label="Local")

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Average Test Accuracy (%)", **font_settings.get("cs_xy_label_font"))

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
    fig.supylabel("The Size of Gradients (MB)", **font_settings.get("cs_xy_label_font"))
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


def plot_ddos_acc(title, fed_sync_sgd, fed_avg, fed_efsign, fed_sign, save_path=None, plot_size="2"):
    font_settings = get_font_settings(plot_size)
    x = range(1, len(fed_sync_sgd) + 1)

    fig, axes = plt.subplots()

    axes.plot(x, fed_sync_sgd, label="BEFS-signSGD", linewidth=3, zorder=10)
    axes.plot(x, fed_efsign, label="EF-signSGD")
    axes.plot(x, fed_sign, label="signSGD")
    axes.plot(x, fed_avg, label="FedAVG")

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Average Test Accuracy (%)", **font_settings.get("cs_xy_label_font"))

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


def plot_time_acc_fall(title, fed_sync_sgd, fed_efsign, fed_avg, save_path=None, plot_size="2"):
    font_settings = get_font_settings(plot_size)
    x = range(1, len(fed_sync_sgd) + 1)

    fig, axes = plt.subplots()

    axes.plot(x, fed_sync_sgd, label="BEFS", linewidth=3, zorder=10)
    axes.plot(x, fed_efsign, label="ARE")
    axes.plot(x, fed_avg, label="FedAVG")

    axes.set_xlabel("Training Round", **font_settings.get("cs_xy_label_font"))
    axes.set_ylabel("Average Test Accuracy (%)", **font_settings.get("cs_xy_label_font"))

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
