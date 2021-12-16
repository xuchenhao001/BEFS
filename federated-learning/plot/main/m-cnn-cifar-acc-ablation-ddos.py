import sys

from plot.utils.time_acc_base import plot_time_acc_ablation

bc_ns = [17.9, 15.37, 32.07, 29.97, 38.6, 37.23, 41.97, 42.77, 44.73, 45.17, 46.97, 47.1, 47.9, 48.6, 48.7, 49.03, 49.5, 50.03, 50.87, 50.5, 50.33, 49.9, 50.1, 49.93, 49.87, 50.4, 50.2, 50.0, 49.8, 49.5, 49.77, 50.07, 50.37, 50.4, 50.23, 50.13, 50.23, 50.23, 50.53, 50.37, 50.3, 50.57, 50.33, 50.17, 50.13, 50.0, 50.23, 49.8, 49.93, 50.0, 49.83, 49.73, 49.73, 49.5, 49.23, 49.5, 49.37, 49.23, 49.23, 49.57, 49.6, 49.33, 49.3, 49.3, 49.27, 49.37, 49.6, 49.23, 49.03, 48.77, 48.97, 48.9, 49.03, 48.8, 48.5, 48.87, 48.87, 48.73, 48.13, 48.13, 48.53, 48.43, 48.4, 48.4, 48.2, 48.3, 48.73, 48.93, 48.8, 49.37, 48.57, 48.63, 48.43, 48.5, 48.4, 48.5, 48.37, 48.1, 48.13, 48.1, 48.17, 47.97, 48.0, 48.03, 48.13, 47.87, 47.8, 47.77, 47.77, 47.73, 47.73, 47.6, 47.6, 47.63, 47.77, 47.6, 47.6, 47.77, 47.8, 47.73, 47.6, 47.97, 48.07, 48.0, 48.03, 48.13, 48.1, 48.3, 48.3, 48.1, 48.07, 48.07, 48.2, 48.17, 48.33, 48.37, 48.4, 48.27, 48.0, 48.07, 48.03, 47.97, 47.9, 47.93, 47.9, 47.73, 47.9, 47.97, 48.07, 48.0, 48.0, 48.0, 48.0, 48.0, 48.03, 48.07, 48.07, 48.07, 48.07, 48.07, 48.07, 48.07, 48.07, 48.07, 48.07, 48.03, 48.0, 48.0, 48.0, 48.07, 48.1, 48.03, 48.03, 48.03, 48.03, 48.07, 48.07, 48.03, 48.03, 48.0, 48.03, 48.03, 48.03, 48.07, 48.07, 48.07, 48.07, 48.03, 48.03, 48.03, 48.03, 48.0, 48.03, 48.03, 48.03, 48.03, 48.03, 48.07, 48.07, 48.07]
bc_FedAvg = [25.1, 37.23, 44.07, 46.43, 50.0, 50.7, 52.8, 53.37, 53.13, 52.9, 52.0, 51.87, 52.0, 52.9, 53.33, 53.23, 53.23, 53.6, 52.93, 53.17, 52.53, 52.43, 52.67, 52.53, 52.4, 51.9, 52.0, 51.83, 51.87, 51.4, 51.63, 51.37, 51.37, 50.83, 50.5, 51.03, 50.27, 50.53, 49.93, 49.5, 50.13, 48.97, 49.7, 49.53, 49.37, 49.63, 49.07, 49.13, 49.5, 48.8, 48.97, 49.03, 49.67, 49.27, 48.3, 48.87, 48.6, 49.3, 49.3, 49.17, 49.1, 49.57, 49.7, 49.27, 49.57, 49.5, 49.43, 49.53, 49.87, 49.97, 49.67, 50.0, 50.03, 49.7, 49.73, 49.8, 49.87, 49.87, 49.73, 49.7, 49.73, 49.43, 49.27, 49.7, 49.77, 49.9, 49.33, 49.47, 49.63, 49.4, 49.47, 49.77, 49.9, 49.8, 49.87, 49.9, 49.83, 49.87, 49.9, 49.93, 49.9, 49.9, 49.93, 49.93, 49.9, 49.9, 50.0, 50.03, 50.03, 50.0, 49.97, 50.0, 50.07, 50.13, 50.13, 50.1, 50.1, 50.07, 50.13, 50.13, 50.13, 50.13, 50.13, 50.2, 50.2, 50.17, 50.2, 50.2, 50.17, 50.17, 50.17, 50.13, 50.13, 50.1, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.23, 50.27, 50.27, 50.27, 50.23, 50.2, 50.2, 50.2, 50.13, 50.13, 50.13, 50.1, 50.1, 50.1, 50.1, 50.13, 50.2, 50.17, 50.17, 50.2, 50.2, 50.2, 50.23, 50.27, 50.27, 50.27, 50.27, 50.23, 50.23, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.2, 50.23, 50.23, 50.23, 50.23, 50.23, 50.23, 50.23, 50.27, 50.27, 50.27, 50.33, 50.33, 50.33, 50.33, 50.33, 50.33, 50.33, 50.33, 50.3, 50.3, 50.3, 50.3, 50.3, 50.3]
ns = [9.1, 9.1, 9.1, 9.1, 12.53, 12.53, 12.53, 28.27, 28.27, 28.27, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 33.17, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 35.97, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 39.87, 41.7, 41.7, 41.7, 41.7, 42.67, 42.67, 42.67, 42.67, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.4, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 42.9, 43.3, 43.3, 43.3, 43.3, 43.3, 43.3, 43.3, 43.3, 43.3, 43.3, 43.3, 43.3, 43.23, 43.23, 43.23, 43.23, 43.23, 43.23, 43.23, 43.23, 43.23, 43.3, 43.3, 43.3, 43.3, 43.3, 43.4, 43.4, 43.33, 43.33, 43.37, 43.37, 43.37, 43.37, 43.37, 43.37, 43.37, 43.37, 43.37, 43.37, 43.37, 43.47, 43.47, 43.5, 43.5, 43.5, 43.5, 43.5, 43.5, 43.5, 43.53, 43.5, 43.5, 43.5, 43.5, 43.5]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc_ablation("", bc_ns, bc_FedAvg, ns, True, False, save_path, plot_size="3")
