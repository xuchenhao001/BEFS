import sys

from plot.utils.time_acc_base import plot_time_bar

sgd = [2.061404228, 0.791707993, 1.66344738]
sign_sgd = [0.096180916, 0.033569336, 0.078927994]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_bar("", sgd, sign_sgd, save_path, plot_size="2")
