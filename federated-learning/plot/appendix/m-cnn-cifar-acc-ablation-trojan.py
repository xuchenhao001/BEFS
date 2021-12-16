import sys

from plot.utils.time_acc_base import plot_time_acc_ablation

bc_ns = [0, 0, 0.03, 2.13, 4.57, 6.57, 18.3, 16.5, 26.83, 23.17, 29.4, 28.6, 33.37, 32.67, 34.03, 31.83, 33.4, 32.63, 34.17, 35.33, 35.27, 35.8, 35.37, 37.7, 36.33, 37.73, 37.3, 37.27, 37.47, 37.63, 35.7, 35.33, 35.3, 36.73, 37.57, 38.07, 37.23, 37.83, 37.97, 38.03, 38.47, 39.43, 40.03, 39.73, 39.53, 41.4, 40.83, 39.97, 39.83, 40.13, 39.63, 41.23, 40.63, 41.5, 41.13, 41.97, 41.67, 41.8, 41.63, 42.47, 41.2, 41.53, 40.37, 41.2, 40.67, 42.47, 41.93, 43.07, 41.73, 41.17, 40.9, 40.47, 40.67, 41.13, 41.97, 42.93, 43.2, 42.87, 41.67, 40.43, 41.27, 42.1, 42.73, 43.87, 43.77, 43.77, 42.57, 42.53, 42.23, 42.6, 41.87, 42.1, 41.23, 42.73, 41.27, 41.3, 41, 42, 42.73, 42.73, 42.53, 42.53, 42.3, 42.2, 42.07, 41.87, 41.8, 41.43, 41.4, 41.37, 41.37, 41.07, 41.57, 42, 42.37, 42.63, 42.67, 43.1, 43.13, 43.37, 43.37, 43.27, 43.43, 43.53, 43.67, 44.07, 44.13, 44.33, 44.47, 44.63, 44.57, 44.77, 45.03, 45.47, 46, 46.33, 46.47, 46.33, 46.53, 46.8, 47.03, 47.1, 47.17, 47.4, 47.4, 47.9, 48.2, 48.83, 48.83, 48.83, 48.83, 48.83, 48.83, 48.93, 48.93, 49.07, 49.13, 49.13, 49.13, 49.07, 49.07, 49.07, 49.07, 49.07, 49.07, 49.07, 49.07, 49.13, 49.13, 49.13, 49.13, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 48.97, 49.07, 49.07, 49.07, 49.07, 49.07]
bc_FedAvg = [0.0, 0.0, 7.23, 9.83, 16.2, 23.5, 30.53, 34.43, 31.1, 34.73, 38.27, 36.33, 36.97, 36.7, 39.83, 34.43, 38.47, 35.23, 38.87, 38.1, 39.63, 38.73, 38.43, 38.63, 38.37, 38.3, 38.8, 39.17, 40.63, 39.4, 41.47, 40.13, 38.83, 38.9, 39.73, 42.0, 41.17, 38.67, 39.73, 38.5, 38.47, 39.23, 40.33, 37.6, 38.5, 37.93, 38.13, 35.77, 37.33, 38.77, 40.9, 39.37, 36.73, 41.6, 37.2, 38.67, 37.73, 40.93, 37.9, 40.53, 39.3, 39.27, 41.07, 39.5, 41.37, 41.77, 39.87, 40.73, 36.1, 39.8, 40.47, 39.1, 41.07, 40.77, 41.7, 41.4, 43.9, 36.87, 45.0, 40.0, 42.97, 39.9, 42.63, 43.23, 41.17, 41.27, 42.9, 44.4, 41.2, 42.8, 42.93, 40.37, 46.93, 41.63, 44.63, 39.4, 40.53, 42.8, 41.23, 46.07, 43.7, 44.5, 43.3, 45.63, 44.7, 41.6, 46.7, 40.37, 45.1, 44.23, 42.23, 45.73, 41.33, 46.03, 41.97, 43.97, 44.5, 42.77, 45.87, 44.63, 45.63, 43.67, 43.57, 44.07, 44.0, 40.13, 44.77, 44.27, 39.73, 42.73, 45.2, 43.53, 44.37, 43.7, 42.73, 41.13, 42.9, 42.13, 44.4, 41.5, 44.0, 42.83, 43.43, 43.37, 38.87, 43.33, 41.5, 43.73, 42.63, 45.97, 42.37, 42.83, 44.53, 39.47, 47.5, 41.9, 43.23, 44.1, 44.03, 44.47, 44.83, 43.57, 41.17, 44.0, 45.97, 44.27, 44.43, 44.27, 43.07, 40.07, 44.33, 41.0, 44.97, 45.4, 43.9, 44.13, 47.3, 42.97, 44.47, 44.53, 43.2, 45.07, 43.9, 44.93, 43.77, 44.9, 41.63, 45.5, 43.97, 45.77, 43.9, 43.1, 42.07, 45.33, 44.1, 40.63, 45.33, 44.03, 41.13, 44.07]
ns = [2.33, 4.4, 0.63, 4.4, 6.3, 13.37, 11.3, 16.43, 19.23, 22.37, 23.0, 23.97, 23.93, 26.4, 27.67, 29.73, 30.17, 30.93, 30.53, 33.0, 33.67, 35.37, 38.1, 39.43, 38.37, 37.3, 36.8, 36.97, 35.83, 34.63, 35.17, 35.73, 35.97, 37.5, 38.87, 39.1, 38.17, 38.3, 37.6, 38.43, 39.3, 39.03, 39.6, 41.77, 41.63, 43.23, 43.2, 42.6, 42.97, 42.57, 41.83, 42.1, 42.37, 41.97, 40.93, 41.17, 40.6, 40.97, 40.7, 41.03, 41.1, 42.6, 43.3, 43.37, 43.63, 43.17, 43.3, 43.43, 43.43, 42.9, 42.4, 42.63, 43.4, 42.87, 43.3, 42.87, 42.83, 43.23, 43.93, 43.1, 44.8, 45.33, 45.4, 45.0, 44.4, 43.07, 42.87, 41.33, 42.3, 43.37, 42.03, 41.6, 41.33, 41.6, 41.97, 43.73, 43.53, 44.03, 42.17, 42.33, 42.43, 42.43, 42.33, 41.97, 41.9, 41.83, 41.63, 41.9, 42.07, 41.97, 42.1, 41.93, 41.67, 41.73, 41.7, 41.37, 40.83, 40.13, 40.13, 39.8, 39.8, 39.73, 40.1, 40.03, 40.33, 39.97, 39.13, 38.57, 38.9, 39.0, 39.07, 39.07, 38.77, 38.6, 38.93, 39.77, 40.3, 40.5, 40.7, 40.9, 41.27, 41.5, 41.73, 42.03, 42.07, 41.97, 42.3, 42.43, 42.93, 43.17, 43.17, 43.4, 43.27, 43.27, 43.4, 43.67, 43.67, 43.73, 43.8, 43.8, 43.8, 43.8, 43.97, 43.97, 44.1, 44.03, 44.0, 44.2, 44.3, 44.23, 44.23, 44.23, 44.23, 44.27, 44.43, 44.43, 44.5, 44.5, 44.5, 44.63, 44.83, 45.17, 45.43, 45.43, 45.43, 45.43, 45.43, 45.43, 45.43, 45.53, 45.53, 45.53, 45.53, 45.53, 45.6, 45.6, 45.6, 45.6, 45.6, 45.6]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc_ablation("", bc_ns, bc_FedAvg, ns, False, False, save_path, plot_size="3")