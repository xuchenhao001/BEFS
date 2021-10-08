import sys

from plot.utils.time_acc_base import plot_time_acc

fed_avg = [65.83, 80.05, 84.27, 85.65, 86.51, 86.61, 87.15, 87.63, 87.69, 87.77, 87.66, 88.2, 88.23, 88.68, 88.6, 88.98, 88.68, 88.79, 88.87, 89.19, 89.01, 89.01, 89.17, 89.22, 89.19, 88.84, 89.03, 89.01, 88.95, 88.84, 89.41, 89.06, 89.3, 88.92, 89.19, 89.49, 89.38, 89.11, 88.92, 89.22, 89.19, 89.38, 89.49, 89.14, 89.17, 89.41, 89.62, 89.35, 88.98, 89.03, 89.17, 89.14, 88.95, 88.98, 89.38, 89.17, 89.33, 89.46, 89.38, 89.38, 89.73, 89.09, 88.84, 89.38, 89.35, 89.52, 89.49, 89.35, 89.09, 89.35, 89.46, 89.27, 89.44, 89.17, 89.41, 89.27, 88.98, 89.3, 89.44, 89.22]
fed_sync = [73.25, 76.99, 79.81, 79.97, 82.02, 81.99, 83.25, 83.04, 83.92, 84.17, 84.65, 85.22, 84.57, 84.76, 85.51, 84.7, 85.22, 85.27, 85.62, 85.51, 86.08, 85.19, 85.7, 86.26, 86.21, 86.05, 85.91, 86.32, 86.48, 86.75, 86.4, 86.85, 86.32, 86.34, 86.56, 86.85, 86.24, 86.53, 86.56, 86.4, 86.4, 86.64, 86.16, 86.53, 86.99, 86.59, 86.42, 86.75, 86.99, 86.42, 86.96, 87.18, 86.75, 86.56, 86.64, 86.96, 86.56, 86.51, 87.1, 86.67, 86.61, 86.94, 86.83, 86.8, 87.12, 87.07, 86.8, 87.07, 87.04, 87.12, 86.96, 86.99, 87.2, 87.34, 87.12, 86.83, 86.88, 87.07, 86.94, 87.12]
fed_sync_sgd = [20.43, 34.38, 48.41, 47.98, 55.97, 38.12, 43.49, 72.88, 45.91, 28.82, 46.45, 45.05, 66.69, 63.2, 26.99, 44.09, 50.13, 62.15, 59.44, 49.54, 50.03, 47.9, 46.77, 49.11, 52.42, 61.69, 51.69, 61.59, 55.65, 71.59, 61.21, 76.13, 63.87, 73.44, 68.55, 33.36, 74.95, 59.09, 73.2, 61.88, 75.08, 75.11, 72.37, 68.84, 73.09, 72.04, 70.83, 68.39, 71.37, 66.53, 76.75, 73.82, 72.02, 69.25, 74.95, 76.21, 76.72, 68.25, 73.33, 74.3, 72.63, 72.12, 79.95, 73.71, 72.85, 74.01, 76.18, 72.58, 68.25, 76.94, 60.99, 75.03, 76.26, 71.32, 75.32, 73.9, 68.28, 77.74, 75.78, 77.07]

save_path = None
if len(sys.argv) == 3 and sys.argv[1] and sys.argv[1] == "save":
    save_path = sys.argv[2]

plot_time_acc("", fed_sync_sgd, fed_sync, fed_avg, save_path, plot_size="L")
