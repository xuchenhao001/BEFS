import sys

from plot.utils.time_acc_base import plot_time_acc

fed_async = [10.18, 10.18, 24.1, 24.82, 53.26, 53.1, 53.1, 83.02, 84.77, 84.77, 86.27, 85.87, 85.78, 85.36, 86.02, 86.02, 85.89, 86.56, 87.7, 87.7, 87.28, 86.64, 86.8, 86.8, 87.12, 87.94, 87.94, 88.42, 87.54, 87.38, 87.38, 87.46, 87.94, 87.86, 87.86, 86.74, 86.99, 87.95, 88.67, 88.26, 88.53, 88.7, 88.3, 88.46, 89.47, 89.76, 89.76, 89.76, 89.22, 89.12, 89.12, 89.3, 88.58, 89.22, 89.22, 89.47, 89.47, 89.23, 89.23, 89.3, 89.01, 89.04, 89.28, 89.41, 89.2, 89.74, 89.82, 89.55, 89.38, 89.25, 89.65, 89.44, 89.2, 88.94, 88.94, 89.33, 89.7, 89.44, 89.44, 89.55, 89.46, 89.62, 89.62, 89.3, 89.31, 89.31, 89.17, 89.33, 89.73, 89.57, 89.41, 89.44, 89.44, 89.44, 89.71, 89.33, 89.33, 89.49]
fed_avg = [9.84, 9.84, 9.84, 9.84, 9.84, 25.6, 41.01, 56.51, 72.14, 87.62, 87.62, 87.62, 87.62, 87.62, 87.86, 88.19, 88.5, 88.72, 89.04, 89.04, 89.04, 89.04, 89.04, 89.28, 89.22, 89.33, 89.25, 89.22, 89.22, 89.22, 89.22, 89.22, 89.22, 88.98, 88.99, 89.04, 88.98, 89.02, 89.02, 89.02, 89.02, 89.02, 89.18, 89.33, 89.36, 89.58, 89.7, 89.7, 89.7, 89.7, 89.7, 89.62, 89.6, 89.55, 89.5, 89.39, 89.39, 89.39, 89.39, 89.39, 89.47, 89.62, 89.65, 89.87, 89.87, 89.87, 89.87, 89.87, 89.87, 89.87, 89.74, 89.84, 89.7, 89.73, 89.73, 89.73, 89.73, 89.73, 89.65, 89.62, 89.55, 89.68, 89.6, 89.6, 89.6, 89.6, 89.6, 89.6, 89.79, 89.79, 89.76, 89.57, 89.57, 89.57, 89.57, 89.57, 89.57, 89.63]
fed_sync = [8.16, 8.16, 8.16, 8.16, 8.16, 86.85, 86.85, 86.85, 86.85, 86.85, 88.06, 88.06, 88.06, 88.06, 88.06, 89.5, 89.5, 89.5, 89.5, 89.5, 89.6, 89.6, 89.6, 89.6, 89.6, 89.95, 89.95, 89.95, 89.95, 89.95, 89.15, 89.15, 89.15, 89.15, 89.15, 89.52, 89.52, 89.52, 89.52, 89.52, 89.86, 89.86, 89.86, 89.86, 89.86, 89.68, 89.68, 89.68, 89.68, 89.68, 89.92, 89.92, 89.92, 89.92, 89.92, 89.7, 89.7, 89.7, 89.7, 89.7, 89.6, 89.6, 89.6, 89.6, 89.6, 89.79, 89.79, 89.79, 89.79, 89.79, 89.98, 89.98, 89.98, 89.98, 89.98, 89.58, 89.58, 89.58, 89.58, 89.58, 89.9, 89.9, 89.9, 89.9, 89.9, 89.6, 89.6, 89.6, 89.6, 89.6, 89.55, 89.55, 89.55, 89.55, 89.55, 89.73, 89.73, 89.73]
fed_localA = [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 24.96, 24.0, 39.74, 39.98, 55.38, 70.45, 70.38, 70.22, 70.22, 54.91, 54.91, 54.91, 54.91, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.32, 24.4, 24.48, 24.48, 24.4, 24.4, 24.32, 24.4, 24.4, 24.32, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4, 24.4]
local_train = [9.74, 24.14, 24.3, 39.09, 68.38, 67.73, 83.42, 84.99, 85.06, 84.74, 85.3, 84.66, 84.85, 85.3, 85.33, 85.34, 85.58, 85.65, 85.73, 85.62, 85.54, 85.15, 86.32, 86.3, 86.38, 86.56, 86.62, 86.98, 86.96, 87.06, 87.08, 87.2, 87.08, 87.02, 87.12, 87.1, 87.04, 87.04, 86.94, 86.94, 86.98, 87.04, 87.04, 87.26, 87.32, 87.2, 87.18, 87.2, 87.22, 87.22, 87.14, 87.06, 87.08, 87.06, 87.08, 87.14, 87.14, 87.02, 87.02, 87.04, 87.04, 87.04, 87.08, 87.08, 87.06, 87.06, 87.12, 87.12, 87.06, 87.06, 87.08, 87.06, 87.06, 87.14, 87.12, 87.08, 87.1, 87.06, 87.02, 87.06, 87.06, 87.06, 87.1, 87.1, 87.04, 87.04, 86.98, 87.02, 87.02, 87.1, 87.1, 86.98, 87.0, 87.04, 87.06, 87.02, 87.02, 87.08]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", 8, 800, fed_async, fed_avg, fed_sync, fed_localA, local_train, save_path, plot_size="S")
